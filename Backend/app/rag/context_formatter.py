from __future__ import annotations

from app.models.schemas import RetrievedChunk


def format_context(chunks: list[RetrievedChunk]) -> str:
    blocks: list[str] = []
    for chunk in chunks:
        blocks.append(f"[source={chunk.source} score={chunk.score:.3f}] {chunk.content}")
    return "\n\n".join(blocks)

