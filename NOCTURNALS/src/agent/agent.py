from .graph import AudioReActGraph
from .ollama_reasoner import OllamaReasoner
from ..rag.store import AudioRAGStore


def create_audio_agent(
    chroma_dir="./data/chroma",
    collection_name="audio_chunks",
    ollama_url="http://127.0.0.1:11434",
    ollama_model="qwen3:8b",
    max_react_steps=4,
):

    rag_store = AudioRAGStore(
        persist_dir=chroma_dir,
        collection_name=collection_name,
    )

    reasoner = OllamaReasoner(
        base_url=ollama_url,
        model=ollama_model,
        timeout=120,
    )

    return AudioReActGraph(
        rag_store=rag_store,
        reasoner=reasoner,
        max_react_steps=max_react_steps,
    )