from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

try:
    from dotenv import load_dotenv  # type: ignore

    load_dotenv(Path(__file__).resolve().parents[1] / ".env", override=False)
except Exception:
    pass


def _resolve_ollama_embedding_model() -> str:
    raw = (os.getenv("OLLAMA_EMBEDDING_MODEL") or os.getenv("EMBEDDING_MODEL") or "nomic-embed-text").strip()
    if raw.lower().startswith("baai/bge-m3"):
        return "bge-m3"
    return raw


@dataclass(frozen=True)
class Settings:
    base_dir: Path = Path(__file__).resolve().parents[1]
    data_dir: Path = Path(os.getenv("DATASET_DIR", r"D:\fyp-6may-final\datasets"))
    audio_dir: Path = Path(os.getenv("AUDIO_DIR", str(Path(__file__).resolve().parents[1] / "audio")))
    chroma_dir: Path = Path(os.getenv("CHROMA_DIR", str(Path(__file__).resolve().parents[1] / "vectorstore" / "chroma_db")))
    embedding_cache_path: Path = Path(
        os.getenv("EMBEDDING_CACHE_PATH", str(Path(__file__).resolve().parents[1] / "vectorstore" / "embedding_cache.json"))
    )

    ollama_base_url: str = os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434").rstrip("/")
    ollama_model: str = os.getenv("OLLAMA_MODEL", "gemma3:4b")
    ollama_timeout_sec: float = float(os.getenv("OLLAMA_TIMEOUT_SEC", "60"))
    ollama_temperature: float = float(os.getenv("OLLAMA_TEMPERATURE", "0.2"))
    ollama_num_predict: int = int(os.getenv("OLLAMA_NUM_PREDICT", "350"))

    # Embeddings via Ollama (default `nomic-embed-text`). `EMBEDDING_MODEL=BAAI/bge-m3` still maps to `bge-m3`.
    ollama_embedding_model: str = _resolve_ollama_embedding_model()
    # urllib can appear to hang on Windows; use requests with (connect, read) timeouts instead.
    ollama_embedding_connect_timeout_sec: float = float(os.getenv("OLLAMA_EMBEDDING_CONNECT_TIMEOUT_SEC", "5"))
    ollama_embedding_read_timeout_sec: float = float(
        os.getenv("OLLAMA_EMBEDDING_READ_TIMEOUT_SEC") or os.getenv("OLLAMA_EMBEDDING_TIMEOUT_SEC") or "120"
    )
    # First /api/embeddings call often loads the model into memory; allow longer read than steady-state.
    ollama_embedding_warmup_read_timeout_sec: float = float(os.getenv("OLLAMA_EMBEDDING_WARMUP_READ_TIMEOUT_SEC", "600"))
    # Kept for .env compatibility; embedding client uses one /api/embeddings call per text.
    ollama_embedding_batch_size: int = int(os.getenv("OLLAMA_EMBEDDING_BATCH_SIZE", "8"))
    ollama_embedding_subbatch: int = int(os.getenv("OLLAMA_EMBEDDING_SUBBATCH", "8"))
    ollama_embedding_max_chars: int = int(os.getenv("OLLAMA_EMBEDDING_MAX_CHARS", "2000"))
    ollama_embedding_l2_normalize: bool = os.getenv("OLLAMA_EMBEDDING_L2_NORMALIZE", "true").lower() in (
        "1",
        "true",
        "yes",
    )

    collection_name: str = os.getenv("CHROMA_COLLECTION", "agri_multilingual_docs")
    retrieval_top_k: int = int(os.getenv("RETRIEVAL_TOP_K", "4"))
    chunk_size: int = int(os.getenv("CHUNK_SIZE", "900"))
    chunk_overlap: int = int(os.getenv("CHUNK_OVERLAP", "180"))
    chroma_upsert_batch_size: int = int(os.getenv("CHROMA_UPSERT_BATCH_SIZE", "4096"))

    whisper_model: str = os.getenv("WHISPER_MODEL_NAME", "medium")
    supported_languages: tuple[str, ...] = ("english", "urdu", "punjabi", "pashto", "sindhi")


settings = Settings()

