"""
Audio utility functions, including playback of WAV files.
"""

from typing import Union

import soundfile as sf


def play_audio(path: Union[str, bytes]) -> None:
    """
    Play the given audio file (WAV recommended).
    (Feature disabled due to system audio dependency)
    """
    print(f"Skipping playback for: {path} (audio playback disabled on server)")


__all__ = ["play_audio"]


