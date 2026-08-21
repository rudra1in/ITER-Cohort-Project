import os
import chromadb
from chromadb.config import Settings

DB_PATH = os.path.join(os.path.dirname(__file__), "../../database/chroma_db")

def get_chroma_client() -> chromadb.PersistentClient:
    os.makedirs(DB_PATH, exist_ok=True)
    return chromadb.PersistentClient(
        path=DB_PATH,
        settings=Settings(allow_reset=True, anonymized_telemetry=False)
    )
