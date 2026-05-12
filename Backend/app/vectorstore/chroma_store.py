from __future__ import annotations

from typing import Any

import chromadb
from chromadb.api.models.Collection import Collection

from app.config import settings
from app.services.ollama_embeddings import ollama_embedding_service


class ChromaStore:
    def __init__(self) -> None:
        settings.chroma_dir.mkdir(parents=True, exist_ok=True)
        self.client = chromadb.PersistentClient(path=str(settings.chroma_dir))
        self.collection = self.client.get_or_create_collection(name=settings.collection_name)

    def _embed(self, texts: list[str]) -> list[list[float]]:
        return ollama_embedding_service.embed_batch(texts)

    def upsert(self, *, ids: list[str], texts: list[str], metadatas: list[dict[str, Any]]) -> None:
        if not ids:
            return
        # Chroma rejects upserts larger than its max batch (~5461 on some builds).
        batch = max(1, min(settings.chroma_upsert_batch_size, 5000))
        for start in range(0, len(ids), batch):
            sl = slice(start, start + batch)
            chunk_ids = ids[sl]
            chunk_texts = texts[sl]
            chunk_metas = metadatas[sl]
            aligned = ollama_embedding_service.embed_documents(chunk_texts)
            ok_ids: list[str] = []
            ok_texts: list[str] = []
            ok_metas: list[dict[str, Any]] = []
            embeddings: list[list[float]] = []
            for _id, _txt, _meta, emb in zip(chunk_ids, chunk_texts, chunk_metas, aligned):
                if emb is None:
                    continue
                ok_ids.append(_id)
                ok_texts.append(_txt)
                ok_metas.append(_meta)
                embeddings.append(emb)
            if not ok_ids:
                continue
            self.collection.upsert(
                ids=list(ok_ids),
                documents=list(ok_texts),
                metadatas=list(ok_metas),
                embeddings=embeddings,
            )

    def query(self, *, text: str, top_k: int) -> dict[str, Any]:
        embedding = self._embed([text])[0]
        return self.collection.query(query_embeddings=[embedding], n_results=top_k, include=["documents", "metadatas", "distances"])

    def count(self) -> int:
        return self.collection.count()

    @property
    def handle(self) -> Collection:
        return self.collection


chroma_store = ChromaStore()

