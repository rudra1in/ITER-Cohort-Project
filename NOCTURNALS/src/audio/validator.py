from pathlib import Path
from pydub import AudioSegment

SUPPORTED_EXTENSIONS = {".wav", ".mp3", ".m4a", ".flac", ".ogg", ".aac"}
MAX_DURATION_SECONDS = 10 * 60


def validate_audio(path: str, max_duration_seconds: int = MAX_DURATION_SECONDS) -> dict:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"Audio file not found: {file_path}")

    if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported audio format: {file_path.suffix}. "
            f"Supported: {sorted(SUPPORTED_EXTENSIONS)}"
        )

    audio = AudioSegment.from_file(file_path)
    duration = len(audio) / 1000.0

    if duration <= 0:
        raise ValueError("Audio duration is zero.")

    if duration > max_duration_seconds:
        raise ValueError(
            f"Audio is {duration:.2f}s long. Maximum allowed duration is "
            f"{max_duration_seconds}s (10 minutes)."
        )

    return {
        "source_file": str(file_path.resolve()),
        "duration": round(duration, 3),
        "sample_rate": audio.frame_rate,
        "channels": audio.channels,
        "format": file_path.suffix.lower().lstrip("."),
    }
