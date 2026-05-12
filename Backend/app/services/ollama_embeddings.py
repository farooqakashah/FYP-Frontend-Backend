from __future__ import annotations

import json
import logging
import math
import os
import re
import time
import unicodedata
from typing import Any

import requests

from app.config import settings

log = logging.getLogger("ollama_embeddings")

EMBEDDINGS_PATH = "/api/embeddings"


def _l2_normalize(vec: list[float]) -> list[float]:
    n = math.sqrt(sum(x * x for x in vec))
    if n <= 0:
        return vec
    return [x / n for x in vec]


_CTRL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")


def _sanitize_text(text: str, *, max_chars: int) -> str:
    t = (text or "").replace("\u0000", " ")
    t = _CTRL_RE.sub(" ", t)
    try:
        t = unicodedata.normalize("NFC", t)
    except Exception:
        pass
    t = " ".join(t.split()).strip()
    if not t:
        return ""
    if len(t) > max_chars:
        t = t[:max_chars]
    return t


def _vector_is_usable(vec: list[float]) -> bool:
    if not vec:
        return False
    for x in vec:
        xf = float(x)
        if math.isnan(xf) or math.isinf(xf):
            return False
    return True


def _clean_vector(vec: list[Any]) -> list[float] | None:
    out: list[float] = []
    for x in vec:
        xf = float(x)
        if math.isnan(xf) or math.isinf(xf):
            out.append(0.0)
        else:
            out.append(xf)
    if all(v == 0.0 for v in out):
        return None
    return out


class OllamaEmbeddingService:
    """
    Embeddings via Ollama using **only** `POST /api/embeddings` with `model` + `prompt`.
    Uses `requests` with explicit connect/read timeouts (avoids urllib hangs on some Windows setups).
    """

    def __init__(self) -> None:
        self.base_url = settings.ollama_base_url
        self.model = settings.ollama_embedding_model
        self._connect_timeout = float(getattr(settings, "ollama_embedding_connect_timeout_sec", 5.0))
        self._read_timeout = float(getattr(settings, "ollama_embedding_read_timeout_sec", 120.0))
        self._warmup_read_timeout = float(getattr(settings, "ollama_embedding_warmup_read_timeout_sec", 600.0))
        self.normalize = settings.ollama_embedding_l2_normalize
        self.max_chars = int(getattr(settings, "ollama_embedding_max_chars", 2000))
        self._session = requests.Session()
        self._warmed_up = False

    def warmup(self) -> None:
        """
        First embedding request often triggers model load (can take minutes). Do it once with a long read timeout.
        """
        if self._warmed_up:
            return
        url = f"{self.base_url}{EMBEDDINGS_PATH}"
        log.info(
            "Ollama embedding warmup: POST %s (model=%s). First load can take several minutes; read_timeout=%ss",
            url,
            self.model,
            self._warmup_read_timeout,
        )
        t0 = time.time()
        payload = {"model": self.model, "prompt": "warmup"}
        try:
            resp = self._session.post(
                url,
                json=payload,
                timeout=(self._connect_timeout, self._warmup_read_timeout),
                headers={"Content-Type": "application/json; charset=utf-8"},
            )
        except requests.Timeout as e:
            raise RuntimeError(
                f"Ollama embedding warmup timed out after {self._warmup_read_timeout}s read. "
                f"Try: `ollama pull {self.model}` then `ollama run {self.model}` once, or increase "
                f"OLLAMA_EMBEDDING_WARMUP_READ_TIMEOUT_SEC. ({e})"
            ) from e
        except requests.RequestException as e:
            raise RuntimeError(f"Ollama embedding warmup failed: {e}") from e
        if resp.status_code != 200:
            detail = (resp.text or "")[:800]
            raise RuntimeError(f"Ollama warmup HTTP {resp.status_code}: {detail}")
        self._warmed_up = True
        log.info("Ollama embedding warmup OK in %.1fs", time.time() - t0)

    def _post_embeddings(self, prompt: str) -> dict[str, Any]:
        if not self._warmed_up:
            self.warmup()
        url = f"{self.base_url}{EMBEDDINGS_PATH}"
        payload = {"model": self.model, "prompt": prompt}
        log.debug(
            "POST %s model=%s prompt_len=%s timeout=(connect=%ss, read=%ss)",
            url,
            self.model,
            len(prompt),
            self._connect_timeout,
            self._read_timeout,
        )
        try:
            resp = self._session.post(
                url,
                json=payload,
                timeout=(self._connect_timeout, self._read_timeout),
                headers={"Content-Type": "application/json; charset=utf-8"},
            )
        except requests.Timeout as e:
            raise RuntimeError(
                f"Ollama embeddings timed out (connect={self._connect_timeout}s read={self._read_timeout}s). "
                f"Is `ollama serve` running and is the embedding model loaded? ({e})"
            ) from e
        except requests.RequestException as e:
            raise RuntimeError(f"Ollama embeddings request failed: {e}") from e

        if resp.status_code != 200:
            detail = (resp.text or "")[:800]
            raise RuntimeError(f"Ollama embedding HTTP {resp.status_code}: {detail}")

        try:
            return resp.json()
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Ollama returned non-JSON: {(resp.text or '')[:400]}") from e

    def _embeddings_one(self, prompt: str) -> list[float]:
        """Single call to /api/embeddings; raises if response is unusable."""
        raw = self._post_embeddings(prompt)
        vec = raw.get("embedding")
        if not isinstance(vec, list):
            raise RuntimeError("Ollama /api/embeddings returned no `embedding` array")
        cleaned = _clean_vector([float(x) for x in vec])
        if cleaned is None or not _vector_is_usable(cleaned):
            raise RuntimeError("Ollama returned embedding with NaN/Inf or all zeros")
        return _l2_normalize(cleaned) if self.normalize else cleaned

    def embed_one_safe(self, text: str) -> list[float]:
        """
        Retry only by shortening/sanitizing the prompt — same endpoint every time.
        """
        limits = [
            min(self.max_chars, 2000),
            min(self.max_chars, 1200),
            min(self.max_chars, 800),
            min(self.max_chars, 400),
            200,
            80,
        ]
        last_err: Exception | None = None
        for lim in limits:
            t = _sanitize_text(text, max_chars=lim)
            if not t:
                continue
            try:
                return self._embeddings_one(t)
            except Exception as e:
                last_err = e
                log.debug("embed retry (limit=%s): %s", lim, e)
        raise RuntimeError(f"Failed to embed after retries. Last error: {last_err}")

    def embed_documents(self, texts: list[str]) -> list[list[float] | None]:
        """
        One HTTP request per document; failures become None (caller skips).
        """
        if not texts:
            return []
        out: list[list[float] | None] = []
        t0 = time.time()
        progress_every = max(1, int(os.getenv("EMBED_PROGRESS_EVERY", "25")))
        for idx, raw in enumerate(texts):
            if idx % progress_every == 0:
                log.info(
                    "Embedding %s/%s chunks (%.1fs elapsed, read_timeout=%ss)",
                    idx + 1,
                    len(texts),
                    time.time() - t0,
                    self._read_timeout,
                )
            try:
                out.append(self.embed_one_safe(raw))
            except Exception as e:
                log.warning(
                    "Skipping embed index=%s: %s | preview=%r",
                    idx,
                    e,
                    (raw or "")[:120],
                )
                out.append(None)
        log.info("Embedding finished %s chunks in %.1fs", len(texts), time.time() - t0)
        return out

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        """Strict: every item must embed or the whole call raises."""
        if not texts:
            return []
        return [self.embed_one_safe(t) for t in texts]


ollama_embedding_service = OllamaEmbeddingService()
