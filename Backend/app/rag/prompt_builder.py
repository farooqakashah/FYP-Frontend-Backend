from __future__ import annotations

from pathlib import Path


def _load_system_prompt() -> str:
    prompt_file = Path(__file__).resolve().parents[1] / "prompts" / "rag_system.txt"
    if prompt_file.exists():
        return prompt_file.read_text(encoding="utf-8")
    return (
        "You are a concise agricultural assistant. "
        "Use only retrieved context. "
        "If context is insufficient, say information was not found in the knowledge base. "
        "Do not expose chain-of-thought."
    )


def build_rag_prompt(user_query_en: str, context: str) -> tuple[str, str]:
    system = _load_system_prompt()
    prompt = (
        "Retrieved context:\n"
        f"{context}\n\n"
        "User question:\n"
        f"{user_query_en}\n\n"
        "Give a short, clear answer."
    )
    return system, prompt

