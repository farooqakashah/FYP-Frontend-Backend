from __future__ import annotations

import shutil
import tempfile
from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.config import settings
from app.models.schemas import ChatRequest, ChatResponse, HealthResponse, TTSRequest, TranscribeResponse
from app.rag.orchestrator import rag_orchestrator
from app.services.translation_service import translation_service
from app.services.tts_service import tts_service
from app.services.whisper_service import whisper_service
from app.vectorstore.chroma_store import chroma_store

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", vector_docs=chroma_store.count(), ollama_model=settings.ollama_model)


@router.post("/transcribe", response_model=TranscribeResponse)
def transcribe(file: UploadFile = File(...)) -> TranscribeResponse:
    suffix = Path(file.filename or "audio.wav").suffix or ".wav"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        shutil.copyfileobj(file.file, tmp)
        temp_path = tmp.name
    try:
        text, detected = whisper_service.transcribe(temp_path)
        translated = text if detected == "english" else translation_service.translate(text, detected, "english")
        return TranscribeResponse(original_text=text, translated_text=translated, detected_language=detected)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    finally:
        Path(temp_path).unlink(missing_ok=True)


@router.post("/tts")
def tts_endpoint(req: TTSRequest) -> dict[str, str]:
    try:
        audio_path = tts_service.synthesize(req.text, req.language)
        return {"audio_path": audio_path}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest) -> ChatResponse:
    try:
        return rag_orchestrator.answer(text=req.text, language=req.language, top_k=req.top_k, with_tts=True)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

