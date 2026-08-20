from pathlib import Path
from pydub import AudioSegment


def preprocess_audio(input_path: str, output_path: str) -> dict:
    """
    Convert to mono, 16 kHz, 16-bit PCM WAV.
    """
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_channels(1).set_frame_rate(16000).set_sample_width(2)

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    audio.export(output, format="wav")

    return {
        "path": str(output),
        "sample_rate": 16000,
        "channels": 1,
        "sample_width": 2,
        "duration": len(audio) / 1000.0,
    }
