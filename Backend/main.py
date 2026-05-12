"""
Main entry point for the multilingual speech-to-speech translation project.

Menu:
    1. Speak → Translate → Listen
    2. Translate existing audio file
    3. Change target language
    4. Exit
"""

import os
from typing import Optional

import audio_utils
import config
import stt
import translate
import tts


def _prompt_int(prompt: str, min_val: int, max_val: int) -> int:
    while True:
        try:
            value = int(input(prompt).strip())
            if min_val <= value <= max_val:
                return value
        except ValueError:
            pass
        print(f"Please enter a number between {min_val} and {max_val}.")


def _choose_target_language() -> None:
    print("\n=== Change Target Language ===")
    languages = ["urdu", "hindi", "english", "punjabi", "sindhi", "pashto"]
    for i, lang in enumerate(languages, start=1):
        print(f"{i}. {lang}")
    choice = _prompt_int("Select target language: ", 1, len(languages))
    config.TARGET_LANGUAGE = languages[choice - 1]
    print(f"Target language set to: {config.TARGET_LANGUAGE}")


def _change_tts_voice() -> None:
    print("\n=== Change TTS Voice ===")
    print("Google TTS automatically selects voices based on language.")
    print("No manual voice configuration is needed.")
    print("Supported languages: English, Urdu, Hindi, Punjabi, Sindhi, Pashto")




def _pipeline_translate_existing_audio() -> None:
    print("\n=== Translate Existing Audio File ===")
    path = input("Enter path to existing audio file (WAV recommended): ").strip()
    if not path:
        print("No path entered.")
        return
    if not os.path.isfile(path):
        print(f"File not found: {path}")
        return

    text, detected_lang_code = stt.speech_to_text(path)
    detected_lang_name = stt.map_whisper_lang_to_name(detected_lang_code)

    print(f"\nDetected language (Whisper): {detected_lang_name} ({detected_lang_code})")
    print(f"Recognized text: {text}")

    if not text:
        print("No text recognized; aborting.")
        return

    target_lang = config.TARGET_LANGUAGE
    print(f"\nTranslating to target language: {target_lang}")
    translated = translate.translate_text(text, target_lang=target_lang)
    print(f"Translated text: {translated}")

    if not translated:
        print("No translated text returned; aborting TTS.")
        return

    output_audio_path = tts.text_to_speech(translated, lang=target_lang, output_path=config.OUTPUT_WAV_PATH)
    audio_utils.play_audio(output_audio_path)


def main() -> None:
    while True:
        print("\n==============================")
        print(" Multilingual S2S Translator ")
        print("==============================")
        print(f"Current target language: {config.TARGET_LANGUAGE}")
        print("1. Translate existing audio file")
        print("2. Change target language")
        print("3. Exit")

        choice = _prompt_int("Select an option: ", 1, 3)

        if choice == 1:
            _pipeline_translate_existing_audio()
        elif choice == 2:
            _choose_target_language()
        elif choice == 3:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()


