from __future__ import annotations

from pydantic import BaseModel, Field


class TranscribeResponse(BaseModel):
    original_text: str
    translated_text: str
    detected_language: str


class ChatRequest(BaseModel):
    text: str = Field(..., min_length=1)
    language: str = Field(default="english")
    top_k: int | None = None


class RetrievedChunk(BaseModel):
    source: str
    score: float
    content: str


class ChatResponse(BaseModel):
    original_text: str
    translated_text: str
    detected_language: str
    retrieved_context: list[RetrievedChunk]
    generated_response: str
    audio_path: str | None = None


class TTSRequest(BaseModel):
    text: str = Field(..., min_length=1)
    language: str = Field(default="english")


class HealthResponse(BaseModel):
    status: str
    vector_docs: int
    ollama_model: str


# Legacy frontend contracts (speech / translate / weather)
class TranslateTextRequest(BaseModel):
    text: str
    target_lang: str
    context_info: str | None = None


class DeleteAudioRequest(BaseModel):
    audio_url: str

