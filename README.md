# 🌾 AI Agriculture Assistant — Multilingual Voice RAG

An AI-powered agricultural assistant that supports **voice and text input** in multiple Pakistani languages (English, Urdu, Punjabi, Sindhi, Pashto). It uses a **RAG (Retrieval-Augmented Generation)** pipeline powered by a local Ollama LLM, OpenAI Whisper for speech recognition, and Edge TTS / gTTS for speech synthesis.

---

## 📁 Project Structure

```
fyp-6may-final/
├── Backend/            # FastAPI backend (API server, STT, TTS, translation, RAG)
│   ├── app/            # Core application package
│   │   ├── api/        # API routes (routes.py, legacy.py)
│   │   ├── embeddings/ # Vectorstore build & loader scripts
│   │   ├── models/     # Pydantic schemas
│   │   ├── prompts/    # Prompt templates
│   │   ├── rag/        # RAG orchestrator, retriever, prompt builder
│   │   ├── services/   # Ollama, Whisper, TTS, translation, embedding services
│   │   ├── utils/      # Shared utilities
│   │   ├── vectorstore/# ChromaDB integration
│   │   ├── config.py   # App-level settings (reads .env)
│   │   └── main.py     # FastAPI app factory
│   ├── config.py       # Root-level config (Ollama, Whisper, TTS paths)
│   ├── stt.py          # Speech-to-text (Whisper)
│   ├── translate.py    # Translation & agricultural QA via Ollama
│   ├── tts.py          # Text-to-speech (Edge TTS / gTTS)
│   ├── api.py          # Entry point for uvicorn
│   ├── requirements.txt
│   └── .env.example    # Environment variable template
├── Front-end/          # React + Vite frontend (chat UI)
│   ├── src/
│   │   ├── components/ # Header, Sidebar, ChatInput, ChatMessage, etc.
│   │   ├── data/       # Suggestion chips per language
│   │   ├── utils/      # Markdown parser
│   │   ├── App.jsx     # Main app with state, recording, text/voice send
│   │   └── main.jsx    # React entry point
│   ├── public/         # Static assets (logo.png, etc.)
│   └── package.json
└── datasets/
    └── pak_sft_train.jsonl  # Agricultural Q&A dataset (used for RAG embeddings)
```

---

## ✅ Prerequisites

Make sure the following are installed on your system **before** running anything:

| Tool | Purpose | Install |
|---|---|---|
| **Python 3.10+** | Backend runtime | [python.org](https://www.python.org/downloads/) |
| **Node.js 18+** | Frontend runtime | [nodejs.org](https://nodejs.org/) |
| **Ollama** | Local LLM inference | [ollama.com](https://ollama.com/) |
| **FFmpeg** | Audio format conversion (WebM → WAV) | [ffmpeg.org](https://ffmpeg.org/download.html) — must be on system `PATH` |
| **Git** | (Optional) Clone the repo | [git-scm.com](https://git-scm.com/) |

> **Windows users:** After installing FFmpeg, add it to your system `PATH`. Verify by running `ffmpeg -version` in a terminal.

---

## 🚀 Quick Start (Step-by-Step)

### Step 1 — Pull Required Ollama Models

Open a terminal and run:

```bash
# Start the Ollama server (leave this running in the background)
ollama serve

# In a NEW terminal window, pull the LLM used for translation & Q&A
ollama pull qwen3.5

# Pull the embedding model used for RAG document retrieval
ollama pull nomic-embed-text
```

> **Note:** `qwen3.5` can be swapped for another model (e.g. `gemma3:4b`) by editing `OLLAMA_MODEL` in `Backend/.env`.

---

### Step 2 — Set Up the Backend

```bash
cd fyp-6may-final/Backend
```

#### 2a. Create & activate a virtual environment

```bash
# Windows (PowerShell)
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

#### 2b. Install Python dependencies

```bash
pip install -r requirements.txt
```

> **Note:** `openai-whisper` will also download the Whisper `medium` model (~1.5 GB) on first use. Ensure you have enough disk space.

#### 2c. Configure environment variables

Copy the example `.env` file and edit it:

```bash
cp .env.example .env
```

Open `Backend/.env` and update as needed:

```env
# Local Ollama LLM (for translation and agricultural Q&A)
OLLAMA_BASE_URL=http://127.0.0.1:11434
OLLAMA_MODEL=qwen3.5

# Embedding model (for RAG retrieval)
OLLAMA_EMBEDDING_MODEL=nomic-embed-text

# Dataset path — update this to your actual absolute path
DATASET_DIR=D:/fyp-6may-final/datasets

# Whisper model size (tiny, base, small, medium, large)
WHISPER_MODEL_NAME=medium

# (Optional) Weather widget — requires a free OpenWeatherMap API key
# OPENWEATHER_API_KEY=your_key_here
```

#### 2d. Build the vector knowledge base (RAG embeddings)

This reads the `.jsonl` dataset and indexes it into ChromaDB. **Only needs to be run once** (or again if the dataset changes):

```bash
# Make sure you're in the Backend directory with venv activated
python -m app.embeddings.build_embeddings
```

This may take several minutes on first run while the embedding model warms up.

#### 2e. Start the Backend server

```bash
uvicorn api:app --reload --host 127.0.0.1 --port 8000
```

The API will be live at **http://127.0.0.1:8000**

- Interactive docs: **http://127.0.0.1:8000/docs**
- Health check: **http://127.0.0.1:8000/health**

---

### Step 3 — Set Up the Frontend

Open a **new terminal window**:

```bash
cd fyp-6may-final/Front-end
```

#### 3a. Install Node.js dependencies

```bash
npm install
```

#### 3b. Start the development server

```bash
npm run dev
```

The frontend will be live at **http://localhost:5173** (or the port shown in the terminal).

---

## 🖥️ Using the Application

Once both servers are running, open your browser to **http://localhost:5173**.

### Interface Features

| Feature | How to Use |
|---|---|
| **Language Selection** | Use the dropdown in the header or sidebar to choose English, اردو, سنڌي, پنجابی, or پښتو |
| **Text Chat** | Type your agricultural question in the input box and press Enter or click Send |
| **Voice Recording** | Click the 🎤 microphone button, speak, then click again to stop. The audio is transcribed, processed, and answered automatically |
| **Audio File Upload** | Upload a `.wav` / `.webm` audio file directly for transcription |
| **Text-to-Speech Playback** | Every AI response includes an audio playback button |
| **Weather Widget** | Click "Get Weather" to fetch local weather data (requires `OPENWEATHER_API_KEY` in `.env`) |
| **Suggestion Chips** | Click any suggested question on the welcome screen to ask it instantly |

### Supported Languages

| Code | Language | Script |
|---|---|---|
| `en` | English | Latin |
| `ur` | Urdu | Nastaliq (RTL) |
| `sd` | Sindhi | Arabic (RTL) |
| `pa` | Punjabi | Shahmukhi (RTL) |
| `ps` | Pashto | Arabic (RTL) |

RTL languages automatically flip the layout direction.

---

## 🔧 API Endpoints Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Service info |
| `GET` | `/health` | Health check (vector doc count + Ollama model) |
| `POST` | `/chat` | Full RAG pipeline — text in → answer + audio out |
| `POST` | `/transcribe` | Upload audio file → transcribed + translated text |
| `POST` | `/tts` | Text → speech audio file |
| `POST` | `/translate-text` | Text + target language → translated answer + audio |
| `POST` | `/speech-to-speech-record` | Uploaded voice → transcribe → answer → audio |
| `GET` | `/weather` | Local weather via OpenWeatherMap (lat/lon params) |
| `DELETE` | `/delete-audio` | Delete a generated audio file |

---

## 🧠 How It Works

```
User Input (text or voice)
       │
       ▼
[Speech-to-Text]  ← Whisper (medium model, local)
       │
       ▼
[Translation to English]  ← Ollama (qwen3.5, local)
       │
       ▼
[RAG Retrieval]  ← ChromaDB + nomic-embed-text embeddings
  (searches pak_sft_train.jsonl knowledge base)
       │
       ▼
[Answer Generation]  ← Ollama (qwen3.5, agricultural expert prompt)
       │
       ▼
[Translation to User's Language]  ← Ollama
       │
       ▼
[Text-to-Speech]  ← Edge TTS (primary) / gTTS (fallback)
       │
       ▼
AI Response (text + audio playback)
```

---

## 🛠️ Troubleshooting

### ❌ `Cannot reach Ollama` error
- Make sure `ollama serve` is running in a terminal.
- Verify the URL: `http://127.0.0.1:11434` (or match `OLLAMA_BASE_URL` in `.env`).

### ❌ `FFmpeg failed` error on voice input
- FFmpeg must be installed and available on your system `PATH`.
- Test: run `ffmpeg -version` in a terminal. If it fails, install FFmpeg.

### ❌ Whisper model not found / slow first start
- On first use, Whisper downloads the `medium` model (~1.5 GB). Wait for it to complete.
- Change `WHISPER_MODEL_NAME=small` in `.env` for faster (but less accurate) transcription.

### ❌ Embeddings build fails
- Ensure `DATASET_DIR` in `.env` points to the folder containing `pak_sft_train.jsonl`.
- Ensure `ollama pull nomic-embed-text` has been run and `ollama serve` is running.
- Run with `--force` to re-index from scratch: `python -m app.embeddings.build_embeddings --force`

### ❌ Weather widget shows error
- Add your OpenWeatherMap API key to `Backend/.env`: `OPENWEATHER_API_KEY=your_key`
- Get a free key at [openweathermap.org/api](https://openweathermap.org/api).

### ❌ Audio plays but sounds wrong (Sindhi/Pashto)
- gTTS doesn't natively support Sindhi or Pashto; the system falls back to Urdu-compatible TTS voices via Edge TTS. This is expected behavior.

---

## 📦 Key Dependencies

### Backend
| Package | Purpose |
|---|---|
| `fastapi` + `uvicorn` | API server |
| `openai-whisper` | Local speech recognition |
| `edge-tts` | Neural TTS (primary) |
| `gtts` | Google TTS (fallback) |
| `pydub` | Audio format conversion |
| `chromadb` | Vector database for RAG |
| `requests` | HTTP client for Ollama embeddings |
| `python-dotenv` | `.env` config loading |

### Frontend
| Package | Purpose |
|---|---|
| `react` + `react-dom` | UI framework |
| `vite` | Dev server & bundler |
| `vite-plugin-pwa` | Progressive Web App support |

---

## 📝 Development Notes

- **Models used:** `qwen3.5` (or `gemma3:4b`) for LLM, `nomic-embed-text` for embeddings, Whisper `medium` for STT.
- **Dataset:** `datasets/pak_sft_train.jsonl` — a multilingual Pakistani agricultural SFT dataset used to build the RAG knowledge base.
- **Audio files** are saved to `Backend/audio/` and served via `/audio/<filename>` static route.
- The frontend talks to the backend at `http://127.0.0.1:8000` (hardcoded). If you change the backend port, update the URLs in `Front-end/src/App.jsx`.
- The app is also configured as a **PWA** (`vite-plugin-pwa`) and can be installed on mobile/desktop browsers.
