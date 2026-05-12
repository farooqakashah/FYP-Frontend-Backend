"""
Legacy HTTP routes expected by the existing frontend (weather, translate+TTS, speech-to-speech).
Keeps paths and response shapes stable; implementation delegates to Backend root modules (stt, translate, tts).
"""

from __future__ import annotations

import os
import shutil
import subprocess
import time
from pathlib import Path

import requests
from fastapi import APIRouter, File, HTTPException, UploadFile

import stt
import translate
import tts
from app.config import settings
from app.models.schemas import DeleteAudioRequest, TranslateTextRequest

router = APIRouter(tags=["legacy"])

_AUDIO_DIR = Path(settings.audio_dir).resolve()


def _convert_to_wav(input_file: str, output_file: str) -> None:
    result = subprocess.run(
        ["ffmpeg", "-y", "-i", input_file, output_file],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        raise RuntimeError(f"FFmpeg failed: {result.stderr.decode(errors='replace')}")


def _needs_script_normalization(text: str) -> bool:
    if not text:
        return False
    if any("\u0900" <= ch <= "\u097F" for ch in text):
        return True
    letters = [ch for ch in text if ch.isalpha()]
    if not letters:
        return False
    ascii_letters = sum(1 for ch in letters if ord(ch) < 128)
    return (ascii_letters / len(letters)) >= 0.6


@router.get("/weather")
def get_weather(lat: float, lon: float):
    api_key = (os.getenv("OPENWEATHER_API_KEY") or "").strip()
    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="OPENWEATHER_API_KEY is not configured on the server.",
        )
    url = "https://api.openweathermap.org/data/2.5/weather"
    try:
        resp = requests.get(
            url,
            params={"lat": lat, "lon": lon, "appid": api_key, "units": "metric"},
            timeout=10,
        )
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Weather service unreachable: {str(e)}") from e

    if resp.status_code != 200:
        if resp.status_code == 401:
            raise HTTPException(
                status_code=502,
                detail="OpenWeatherMap rejected the API key (401). Verify the key / plan / API access.",
            )
        try:
            detail = resp.json()
        except Exception:
            detail = resp.text
        raise HTTPException(
            status_code=502,
            detail={
                "message": "OpenWeatherMap request failed",
                "upstream_status": resp.status_code,
                "upstream_detail": detail,
            },
        )

    try:
        data = resp.json()
        return {
            "city": data.get("name"),
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": (data.get("weather") or [{}])[0].get("description"),
        }
    except Exception:
        raise HTTPException(status_code=502, detail="Unexpected response from weather provider")


@router.post("/translate-text")
def translate_text_api(req: TranslateTextRequest):
    translated = translate.translate_text(req.text, req.target_lang)

    rel = f"output_{int(time.time())}.wav"
    filename = str(_AUDIO_DIR / rel)
    tts.text_to_speech(translated, lang=req.target_lang, output_path=filename)
    tts_engine = getattr(tts, "get_last_tts_engine_info", lambda: "Unknown")()

    return {
        "translated_text": translated,
        "tts_engine": tts_engine,
        "audio_url": f"/audio/{rel}",
    }


@router.delete("/delete-audio")
def delete_audio(req: DeleteAudioRequest):
    audio_url = (req.audio_url or "").strip()
    if not audio_url:
        raise HTTPException(status_code=400, detail="audio_url is required")

    rel = audio_url.lstrip("/")
    if rel.startswith("audio/"):
        rel = rel[len("audio/") :]

    fname = os.path.basename(rel)
    if not fname.lower().endswith(".wav"):
        raise HTTPException(status_code=400, detail="Only .wav files can be deleted")
    if not fname.startswith("output_"):
        raise HTTPException(status_code=403, detail="Not allowed to delete this file")

    path = (_AUDIO_DIR / fname).resolve()
    try:
        path.relative_to(_AUDIO_DIR)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid audio path") from None

    if not path.exists():
        return {"deleted": False, "reason": "not_found", "file": fname}

    try:
        path.unlink()
        return {"deleted": True, "file": fname}
    except OSError as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete file: {str(e)}") from e


@router.post("/speech-to-speech-record")
def speech_to_speech_record(
    file: UploadFile = File(...),
    target_lang: str = "urdu",
):
    input_path = f"temp_{int(time.time())}.webm"
    wav_path = f"temp_{int(time.time())}.wav"

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        _convert_to_wav(input_path, wav_path)
        target_lang = target_lang.lower().strip()
        text, detected_lang = stt.speech_to_text(wav_path, target_lang=target_lang)

        if not text:
            return {"error": "No speech detected"}

        translated = translate.translate_text(text, target_lang)

        display_text = text
        normalizer = getattr(translate, "normalize_transcript_for_display", None)
        if callable(normalizer):
            if target_lang == "pashto":
                display_text = normalizer(text, target_lang)
            elif _needs_script_normalization(text) and target_lang in {"urdu", "sindhi", "punjabi", "balochi"}:
                display_text = normalizer(text, target_lang)

        rel = f"output_{int(time.time())}.wav"
        out_path = str(_AUDIO_DIR / rel)
        tts.text_to_speech(translated, lang=target_lang, output_path=out_path)
        tts_engine = getattr(tts, "get_last_tts_engine_info", lambda: "Unknown")()

        return {
            "original_text": display_text,
            "detected_language": detected_lang,
            "target_language": target_lang,
            "translated_text": translated,
            "tts_engine": tts_engine,
            "audio_url": f"/audio/{rel}",
        }
    finally:
        if os.path.exists(input_path):
            os.remove(input_path)
        if os.path.exists(wav_path):
            os.remove(wav_path)
