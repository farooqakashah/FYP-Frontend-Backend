"""
Configuration for the multilingual speech-to-speech translation project.
Edit this file to change defaults for target language, model paths, and API endpoints.
"""

import os
from pathlib import Path

# Load `.env` beside this file (`Backend/.env`) for optional overrides.
try:
    from dotenv import load_dotenv  # type: ignore

    _BACKEND_DOTENV = Path(__file__).resolve().with_name(".env")
    load_dotenv(dotenv_path=_BACKEND_DOTENV, override=True)
except Exception:
    pass

# =========================
# Ollama (local LLM, e.g. Qwen 3.5)
# =========================

OLLAMA_BASE_URL: str = (os.getenv("OLLAMA_BASE_URL") or "http://127.0.0.1:11434").strip().rstrip("/")
OLLAMA_MODEL: str = (os.getenv("OLLAMA_MODEL") or "qwen3.5").strip()
OLLAMA_MODEL_FALLBACK: str = (os.getenv("OLLAMA_MODEL_FALLBACK") or "").strip()
OLLAMA_TIMEOUT_SEC: float = float(os.getenv("OLLAMA_TIMEOUT_SEC", "120"))

# Conversation: keep answers short — caps output tokens (`num_predict` in Ollama).
OLLAMA_NUM_PREDICT_CHAT: int = int(os.getenv("OLLAMA_NUM_PREDICT_CHAT", "512"))
OLLAMA_NUM_PREDICT_UTIL: int = int(os.getenv("OLLAMA_NUM_PREDICT_UTIL", "4096"))

# Thinking/reasoning: always off at the API (`think: false`) for fast dialogue; see translate.py.

# Target language for translation (logical language name, not locale code)
TARGET_LANGUAGE: str = "urdu"

# Legacy name kept for readability (same default as OLLAMA_MODEL for local Qwen setups).
QWEN_MODEL_NAME: str = OLLAMA_MODEL

# =========================
# Whisper configuration
# =========================

WHISPER_MODEL_NAME: str = "medium"
SAMPLE_RATE: int = 16000
DEFAULT_RECORD_SECONDS: int = 10

# =========================
# Google TTS configuration
# =========================

OUTPUT_WAV_PATH: str = os.path.join(os.path.dirname(__file__), "output.wav")
TEMP_INPUT_WAV_PATH: str = os.path.join(os.path.dirname(__file__), "input.wav")

