from __future__ import annotations

from app.models.schemas import ChatResponse
from app.rag.context_formatter import format_context
from app.rag.prompt_builder import build_rag_prompt
from app.rag.retriever_service import retriever_service
from app.services.ollama_service import ollama_service
from app.services.translation_service import translation_service
from app.services.tts_service import tts_service


class RagOrchestrator:
    def answer(self, *, text: str, language: str, top_k: int | None = None, with_tts: bool = True) -> ChatResponse:
        normalized_language = translation_service.normalize_language(language)
        query_en = translation_service.translate(text, normalized_language, "english")
        chunks = retriever_service.retrieve(query_en, top_k=top_k)

        strong_chunks = [c for c in chunks if c.score >= 0.15]

        if not strong_chunks:
            fallback = "I could not find this information in the available knowledge base."
            final_response = (
                fallback if normalized_language == "english" else translation_service.translate(fallback, "english", normalized_language)
            )
            audio_path = tts_service.synthesize(final_response, normalized_language) if with_tts else None
            return ChatResponse(
                original_text=text,
                translated_text=query_en,
                detected_language=normalized_language,
                retrieved_context=chunks,
                generated_response=final_response,
                audio_path=audio_path,
            )

        context = format_context(strong_chunks)
        system, prompt = build_rag_prompt(query_en, context)
        response_en = ollama_service.generate(prompt=prompt, system_prompt=system)
        if not response_en:
            response_en = "I could not find this information in the available knowledge base."

        final_response = (
            response_en
            if normalized_language == "english"
            else translation_service.translate(response_en, "english", normalized_language)
        )
        audio_path = tts_service.synthesize(final_response, normalized_language) if with_tts else None
        return ChatResponse(
            original_text=text,
            translated_text=query_en,
            detected_language=normalized_language,
            retrieved_context=strong_chunks,
            generated_response=final_response,
            audio_path=audio_path,
        )


rag_orchestrator = RagOrchestrator()

