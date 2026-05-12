from __future__ import annotations

import json
import urllib.error
import urllib.request

from app.config import settings


class OllamaService:
    def __init__(self) -> None:
        self.base_url = settings.ollama_base_url
        self.default_model = settings.ollama_model
        self.timeout = settings.ollama_timeout_sec

    def generate(
        self,
        *,
        prompt: str,
        system_prompt: str,
        model: str | None = None,
        temperature: float | None = None,
        num_predict: int | None = None,
    ) -> str:
        request_model = model or self.default_model
        payload = {
            "model": request_model,
            "stream": False,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            "think": False,
            "options": {
                "temperature": settings.ollama_temperature if temperature is None else temperature,
                "num_predict": settings.ollama_num_predict if num_predict is None else num_predict,
            },
        }
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            f"{self.base_url}/api/chat",
            data=data,
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                body = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")[:600]
            raise RuntimeError(f"Ollama error {exc.code}: {detail}") from exc
        except urllib.error.URLError as exc:
            raise RuntimeError(f"Could not connect to Ollama at {self.base_url}") from exc
        return ((body.get("message") or {}).get("content") or "").strip()


ollama_service = OllamaService()

