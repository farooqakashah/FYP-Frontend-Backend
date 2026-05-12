from __future__ import annotations

from app.config import settings
from app.models.schemas import RetrievedChunk
from app.vectorstore.chroma_store import chroma_store


class RetrieverService:
    def retrieve(self, query: str, top_k: int | None = None) -> list[RetrievedChunk]:
        k = top_k or settings.retrieval_top_k
        result = chroma_store.query(text=query, top_k=k)
        docs = (result.get("documents") or [[]])[0]
        metas = (result.get("metadatas") or [[]])[0]
        distances = (result.get("distances") or [[]])[0]

        chunks: list[RetrievedChunk] = []
        for idx, content in enumerate(docs):
            meta = metas[idx] if idx < len(metas) else {}
            distance = float(distances[idx]) if idx < len(distances) else 1.0
            score = max(0.0, 1.0 - distance)
            chunks.append(
                RetrievedChunk(
                    source=str(meta.get("source", "unknown")),
                    score=score,
                    content=content,
                )
            )
        return chunks


retriever_service = RetrieverService()

