"""
Remove persisted Chroma data and the incremental embedding file cache.

Run from Backend:
    python -m app.embeddings.clean_vectorstore

Stop any running uvicorn/FastAPI process using the same Chroma path first.
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

from app.config import settings


def clean_vectorstore() -> dict[str, str]:
    removed: list[str] = []
    chroma = settings.chroma_dir.resolve()
    if chroma.exists():
        shutil.rmtree(chroma)
        removed.append(str(chroma))
    chroma.mkdir(parents=True, exist_ok=True)

    cache = settings.embedding_cache_path.resolve()
    if cache.exists():
        cache.unlink()
        removed.append(str(cache))

    return {"status": "ok", "removed": removed}


if __name__ == "__main__":
    try:
        out = clean_vectorstore()
        print(json.dumps(out, indent=2))
    except OSError as e:
        print(f"Error: {e}", file=sys.stderr)
        print("Close any process holding the Chroma folder and retry.", file=sys.stderr)
        sys.exit(1)
