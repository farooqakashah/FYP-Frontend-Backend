from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

SUPPORTED_EXTENSIONS = {".jsonl"}


def iter_dataset_files(root: Path) -> list[Path]:
    files: list[Path] = []
    if root.is_file() and root.suffix.lower() in SUPPORTED_EXTENSIONS:
        return [root]
    for path in root.rglob("*.jsonl"):
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS:
            files.append(path)
    return files


def read_file_content(path: Path) -> str:
    # Legacy compatibility. For the redo we operate at JSONL-record level via `iter_jsonl_records`.
    return path.read_text(encoding="utf-8", errors="ignore")


def iter_jsonl_records(path: Path) -> Iterable[tuple[int, dict[str, Any]]]:
    """
    Yields (line_index, json_object) for a JSONL file.
    Skips blank/invalid lines instead of failing the whole run.
    """
    with path.open("r", encoding="utf-8", errors="ignore") as handle:
        for i, line in enumerate(handle):
            if not line.strip():
                continue
            try:
                obj = json.loads(line)
                if isinstance(obj, dict):
                    yield i, obj
            except Exception:
                continue


def record_to_text(record: dict[str, Any]) -> str:
    """
    Convert a dataset record into a retrieval-friendly text block.
    Supports common SFT shapes:
    - {instruction, input, output}
    - {question, answer}
    - {prompt, response}
    - {messages: [{role, content}, ...]}
    Falls back to JSON string if unknown.
    """
    for qk, ak in (("question", "answer"), ("prompt", "response"), ("instruction", "output")):
        q = record.get(qk)
        a = record.get(ak)
        if isinstance(q, str) and isinstance(a, str):
            inp = record.get("input")
            extra = f"\nContext: {inp.strip()}" if isinstance(inp, str) and inp.strip() else ""
            return f"Q: {q.strip()}{extra}\nA: {a.strip()}"

    msgs = record.get("messages")
    if isinstance(msgs, list) and msgs:
        parts: list[str] = []
        for m in msgs:
            if not isinstance(m, dict):
                continue
            role = str(m.get("role") or "").strip()
            content = m.get("content")
            if not isinstance(content, str):
                continue
            if role:
                parts.append(f"{role.upper()}: {content.strip()}")
            else:
                parts.append(content.strip())
        if parts:
            return "\n".join(parts)

    return json.dumps(record, ensure_ascii=False)


def chunk_text(text: str, *, chunk_size: int, overlap: int) -> list[str]:
    clean = " ".join((text or "").split())
    if not clean:
        return []
    out: list[str] = []
    start = 0
    step = max(1, chunk_size - overlap)
    while start < len(clean):
        out.append(clean[start : start + chunk_size])
        start += step
    return out

