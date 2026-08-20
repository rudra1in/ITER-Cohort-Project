# Local Audio Detection Agent

A fully local prototype for the AI-proctoring audio pipeline.

Stages:
1. Audio validation + preprocessing
2. Efficient 5-second chunking with 1-second overlap
3. Local ChromaDB storage/retrieval
4. LangGraph bounded ReAct reasoning loop using Ollama
5. Structured proctoring report

## Important design

The audio detector is deliberately lightweight and offline:
- VAD-like energy/silence analysis
- spectral features
- simple heuristic event classifier

The Ollama model is the reasoning/controller layer. It does NOT receive raw audio.
It receives structured acoustic evidence and may request:
- LABEL
- RETRIEVE_CONTEXT
- RE_ANALYZE
- REVIEW
- STORE
- NEXT_CHUNK
- END

This makes the prototype runnable without a cloud audio API.

## Prerequisites

Python 3.10+ recommended.

Install FFmpeg and make sure `ffmpeg` is available on PATH because pydub uses it for
common formats such as MP3/M4A. WAV files work best for the first test.

Install Ollama, then:

    ollama pull qwen3:8b
    ollama pull nomic-embed-text

Start Ollama:

    ollama serve

## Windows setup

    py -3.10 -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt
    copy .env.example .env

Run:

    python -m src.runner_audio_agent --audio path\to\test.wav

Or:

    python -m src.runner_audio_agent --audio path\to\test.mp3

## Output

Chunks:
    storage/audio/<audio_id>/chunk_XXXX.wav

Metadata/index:
    data/chroma/

Report:
    data/audio_reports/<audio_id>_report.json

## Event labels

KEYBOARD
HUMAN_SPEECH
MULTIPLE_VOICES
VEHICLE_NOISE
ENVIRONMENTAL_NOISE
SILENCE
OTHER

This is a prototype detector, not a production-grade forensic classifier. The ReAct
loop is real and bounded, but the acoustic classifier should later be replaced with
a trained sound-event model if higher detection accuracy is required.
