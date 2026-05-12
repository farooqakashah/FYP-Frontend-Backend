from __future__ import annotations

import hashlib
from pathlib import Path

import tts

from app.config import settings
from app.services.translation_service import translation_service


class TTSService:
    def __init__(self) -> None:
        settings.audio_dir.mkdir(parents=True, exist_ok=True)

    def synthesize(self, text: str, language: str) -> str:
        normalized_lang = translation_service.normalize_language(language)
        key = hashlib.sha1(f"{normalized_lang}:{text}".encode("utf-8")).hexdigest()[:20]
        output_path = settings.audio_dir / f"{key}.wav"
        if output_path.exists():
            return str(output_path)
        generated = tts.text_to_speech(text=text, lang=normalized_lang, output_path=str(output_path))
        return str(Path(generated).resolve())


tts_service = TTSService()

