from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.legacy import router as legacy_router
from app.api.routes import router
from app.config import settings

settings.audio_dir.mkdir(parents=True, exist_ok=True)

app = FastAPI(title="Multilingual Voice RAG API", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/audio", StaticFiles(directory=str(settings.audio_dir)), name="audio")


@app.get("/")
def root() -> dict[str, str]:
    return {
        "service": "Multilingual Voice RAG API",
        "docs": "/docs",
        "health": "/health",
    }


app.include_router(router)
app.include_router(legacy_router)

