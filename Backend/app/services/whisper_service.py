from __future__ import annotations

from typing import Optional

import stt

from app.services.translation_service import translation_service


class WhisperService:
    def transcribe(self, audio_path: str, target_lang: Optional[str] = None) -> tuple[str, str]:
        text, lang_code = stt.speech_to_text(audio_path, target_lang=target_lang)
        detected = translation_service.normalize_language(stt.map_whisper_lang_to_name(lang_code))
        return text, detected


whisper_service = WhisperService()

