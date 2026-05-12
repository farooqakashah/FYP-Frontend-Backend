"""
Backward-compatible API module.
Use `app.main:app` for the production-ready multilingual RAG API.
"""

from app.main import app

__all__ = ["app"]


