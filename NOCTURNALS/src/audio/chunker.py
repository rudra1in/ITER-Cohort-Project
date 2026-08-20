from pathlib import Path
import wave


def _wav_duration(path: str) -> float:
    with wave.open(path, "rb") as wf:
        return wf.getnframes() / float(wf.getframerate())


def _slice_wav(input_path: str, output_path: str, start: float, end: float) -> None:
    with wave.open(input_path, "rb") as src:
        params = src.getparams()
        rate = src.getframerate()
        start_frame = int(start * rate)
        end_frame = int(end * rate)

        src.setpos(min(start_frame, src.getnframes()))
        frames = src.readframes(max(0, end_frame - start_frame))

        with wave.open(output_path, "wb") as dst:
            dst.setparams(params)
            dst.writeframes(frames)


def chunk_audio(
    wav_path: str,
    output_dir: str,
    chunk_seconds: float = 5.0,
    overlap_seconds: float = 1.0,
) -> list[dict]:
    """
    Fixed windows with overlap.

    Example:
      chunk 0 = 0-5
      chunk 1 = 4-9
      chunk 2 = 8-13
    """
    if overlap_seconds >= chunk_seconds:
        raise ValueError("overlap_seconds must be smaller than chunk_seconds.")

    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    duration = _wav_duration(wav_path)
    step = chunk_seconds - overlap_seconds

    chunks = []
    start = 0.0
    index = 0

    while start < duration:
        end = min(start + chunk_seconds, duration)
        if end <= start:
            break

        chunk_path = output / f"chunk_{index:04d}.wav"
        _slice_wav(wav_path, str(chunk_path), start, end)

        chunks.append(
            {
                "chunk_id": f"chunk_{index:04d}",
                "chunk_index": index,
                "start_timestamp": round(start, 3),
                "end_timestamp": round(end, 3),
                "duration": round(end - start, 3),
                "storage_path": str(chunk_path),
                "processing_status": "PENDING",
            }
        )

        index += 1
        start += step

    return chunks
