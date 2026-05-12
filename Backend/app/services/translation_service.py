from __future__ import annotations

import re

from app.services.ollama_service import ollama_service

LANGUAGE_ALIASES = {
    "en": "english",
    "ur": "urdu",
    "pa": "punjabi",
    "ps": "pashto",
    "sd": "sindhi",
}

_SINDHI_PUNJABI_DRIFT_TOKENS: tuple[str, ...] = (
    "۾",
    "۽",
    "آهي",
    "آھن",
    "آهن",
    "جي",
)
_PUNJABI_NORMALIZE_MAP: tuple[tuple[str, str], ...] = (
    (" ۾ ", " وچ "),
    ("۾", " وچ "),
    (" ۽ ", " تے "),
    ("۽", " تے "),
    ("آهي", "اے"),
    ("آھن", "نے"),
    ("آهن", "نے"),
    ("ٿ", "ت"),
    ("ڀ", "بھ"),
    ("ڇ", "چ"),
    ("ٻ", "ب"),
    ("ڪ", "کھ"),
    ("ڳ", "گ"),
    ("ڱ", "نگ"),
    ("ڻ", "ن"),
    ("ڏ", "ڈ"),
    ("ڊ", "ڈ"),
    ("ڍ", "ڈ"),
    ("ڌ", "د"),
    ("ڄ", "ج"),
    ("ڃ", "ج"),
    ("ڦ", "پھ"),
)


class TranslationService:
    def normalize_language(self, language: str) -> str:
        key = (language or "").strip().lower()
        return LANGUAGE_ALIASES.get(key, key or "english")

    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        if not text:
            return ""
        source = self.normalize_language(source_lang)
        target = self.normalize_language(target_lang)
        if source == target:
            return text

        system = (
            "You are a strict translator. Return only the translated text. "
            "Do not add explanations, role markers, or chain-of-thought."
        )
        if target == "punjabi":
            prompt = (
                f"Translate the following text from {source} into Pakistani Punjabi written in Shahmukhi "
                "(Arabic/Perso-Arabic script).\n\n"
                "Rules:\n"
                "- Output ONLY Punjabi Shahmukhi text.\n"
                "- Do NOT use Gurmukhi script.\n"
                "- Do NOT use Devanagari script.\n"
                "- Do NOT write Sindhi.\n"
                "- Preserve meaning exactly.\n\n"
                f"Text:\n{text}"
            )
        else:
            prompt = f"Translate the following text from {source} to {target}:\n\n{text}"
        translated = ollama_service.generate(prompt=prompt, system_prompt=system, temperature=0.0, num_predict=300)

        if target == "punjabi" and (self._looks_like_sindhi(translated) or self._has_wrong_script_for_punjabi(translated)):
            repair_prompt = (
                "Rewrite this text into Punjabi Shahmukhi (Pakistan Punjabi) only. "
                "Use ONLY Arabic/Perso-Arabic script used in Pakistan. "
                "Do NOT use Gurmukhi. Do NOT use Devanagari. Do NOT write Sindhi. "
                "Preserve exact meaning. Return only rewritten Punjabi text.\n\n"
                f"{translated}"
            )
            repaired = ollama_service.generate(
                prompt=repair_prompt,
                system_prompt=system,
                temperature=0.0,
                num_predict=300,
            )
            if repaired and (not self._looks_like_sindhi(repaired)) and (not self._has_wrong_script_for_punjabi(repaired)):
                return self._normalize_punjabi_shahmukhi(repaired)

            # Final fallback: explicitly convert Sindhi-like output into Punjabi Shahmukhi.
            second_repair_prompt = (
                "Convert this Sindhi-like text into natural Punjabi Shahmukhi (Pakistani Punjabi in Arabic script). "
                "Do NOT use Sindhi words or grammar. Preserve meaning exactly. Output only Punjabi Shahmukhi text.\n\n"
                f"{repaired or translated}"
            )
            second_repaired = ollama_service.generate(
                prompt=second_repair_prompt,
                system_prompt=system,
                temperature=0.0,
                num_predict=300,
            )
            if second_repaired and (not self._looks_like_sindhi(second_repaired)) and (
                not self._has_wrong_script_for_punjabi(second_repaired)
            ):
                return self._normalize_punjabi_shahmukhi(second_repaired)
        if target == "punjabi":
            return self._normalize_punjabi_shahmukhi(translated)
        return translated

    def _looks_like_sindhi(self, text: str) -> bool:
        if not text:
            return False
        token_hits = sum(1 for token in _SINDHI_PUNJABI_DRIFT_TOKENS if token in text)
        # Sindhi-only letter block that should not appear repeatedly in Punjabi Shahmukhi output.
        char_hits = len(re.findall(r"[ڄڃٻڪڳڱٺڏڊڍڌ]", text))
        return token_hits >= 1 or char_hits >= 2

    def _has_wrong_script_for_punjabi(self, text: str) -> bool:
        if not text:
            return False
        # Gurmukhi or Devanagari means wrong script for Pakistani Punjabi (Shahmukhi).
        return bool(re.search(r"[\u0A00-\u0A7F\u0900-\u097F]", text))

    def _normalize_punjabi_shahmukhi(self, text: str) -> str:
        if not text:
            return text
        out = text
        for src, dst in _PUNJABI_NORMALIZE_MAP:
            out = out.replace(src, dst)
        return " ".join(out.split())


translation_service = TranslationService()

