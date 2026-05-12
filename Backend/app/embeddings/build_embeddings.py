from __future__ import annotations

import hashlib
import json
import logging
import os
import sys
import time
from pathlib import Path
from typing import Any

from app.config import settings
from app.embeddings.loader import chunk_text, iter_dataset_files, iter_jsonl_records, record_to_text
from app.vectorstore.chroma_store import chroma_store


def _file_signature(path: Path) -> dict[str, Any]:
    stat = path.stat()
    return {"mtime": stat.st_mtime, "size": stat.st_size}


def _load_cache(cache_path: Path) -> dict[str, Any]:
    if not cache_path.exists():
        return {"files": {}}
    return json.loads(cache_path.read_text(encoding="utf-8"))


def _save_cache(cache_path: Path, cache_data: dict[str, Any]) -> None:
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(cache_data, ensure_ascii=False, indent=2), encoding="utf-8")


def _get_logger() -> logging.Logger:
    log = logging.getLogger("embeddings")
    if log.handlers:
        return log
    level = logging.INFO
    level_name = (os.getenv("EMBED_DEBUG_LEVEL") or "").strip().upper()
    if level_name in {"DEBUG", "INFO", "WARNING", "ERROR"}:
        level = getattr(logging, level_name)
    logging.basicConfig(level=level, format="[%(levelname)s] %(message)s")
    return log


def build_embeddings(*, force: bool = False) -> dict[str, int]:
    dataset_root = settings.data_dir
    cache_path = settings.embedding_cache_path
    cache = _load_cache(cache_path)

    processed_files = 0
    embedded_chunks = 0
    files = iter_dataset_files(dataset_root)
    log = _get_logger()

    if len(files) != 1:
        raise RuntimeError(f"Expected exactly 1 .jsonl file in {dataset_root}, found {len(files)}: {files}")

    for path in files:
        t0 = time.time()
        log.info(f"Processing JSONL: {path}")
        source = str(path.resolve())
        signature = _file_signature(path)
        if (not force) and cache["files"].get(source) == signature:
            log.info("Cache hit: no changes detected. Skipping.")
            continue

        ids: list[str] = []
        docs: list[str] = []
        metadatas: list[dict[str, Any]] = []

        rec_count = 0
        bad_records = 0
        empty_records = 0
        for line_idx, record in iter_jsonl_records(path):
            rec_count += 1
            try:
                text_block = record_to_text(record)
            except Exception:
                bad_records += 1
                continue

            chunks = chunk_text(text_block, chunk_size=settings.chunk_size, overlap=settings.chunk_overlap)
            if not chunks:
                empty_records += 1
                continue

            for chunk_idx, chunk in enumerate(chunks):
                chunk_id = hashlib.sha1(f"{source}:{line_idx}:{chunk_idx}:{chunk[:120]}".encode("utf-8")).hexdigest()
                ids.append(chunk_id)
                docs.append(chunk)
                metadatas.append(
                    {
                        "source": source,
                        "jsonl_line": line_idx,
                        "chunk_index": chunk_idx,
                        "record_index": rec_count - 1,
                        "language": "multilingual",
                    }
                )

            if rec_count % 1000 == 0:
                log.debug(f"records={rec_count} prepared_chunks={len(ids)} last_line={line_idx}")

        log.info(
            f"Parsed records={rec_count} bad_records={bad_records} empty_records={empty_records} total_chunks={len(ids)}"
        )
        if docs:
            log.debug(f"Chunk[0] preview: {docs[0][:220]!r}")

        up0 = time.time()
        chroma_store.upsert(ids=ids, texts=docs, metadatas=metadatas)
        log.info(f"Chroma upsert finished in {time.time() - up0:.2f}s")

        cache["files"][source] = signature
        processed_files += 1
        embedded_chunks += len(ids)
        log.info(f"Done in {time.time() - t0:.2f}s. chunks_indexed={len(ids)}")

    _save_cache(cache_path, cache)
    return {"processed_files": processed_files, "embedded_chunks": embedded_chunks}


if __name__ == "__main__":
    force = "--force" in sys.argv
    result = build_embeddings(force=force)
    print(json.dumps(result, indent=2))

