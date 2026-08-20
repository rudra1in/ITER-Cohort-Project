import os
import sys
import psycopg2
from pathlib import Path
from dotenv import load_dotenv
from ollama import Client   # ✅ Ollama client

# ============================================================
# 1. LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

# Ollama doesn’t need an API key like Gemini, but we keep dotenv for consistency
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "nomic-embed-text")

# ============================================================
# 2. OLLAMA CLIENT
# ============================================================

client = Client()

# ============================================================
# 3. IMPORT INGESTION MODULES
# ============================================================

INGESTION_DIR = Path(__file__).parent.parent / "ingestion"
sys.path.append(str(INGESTION_DIR))

from document_loader import load_documents
from chunking import create_chunks

# ============================================================
# 4. GENERATE EMBEDDING
# ============================================================

def get_embedding(text):
    response = client.embeddings(model=OLLAMA_MODEL, prompt=text)
    return response["embedding"]  # ✅ 768 dimensions

# ============================================================
# 5. STORE EMBEDDINGS IN POSTGRESQL
# ============================================================

def store_embeddings(chunks):
    conn = psycopg2.connect(
        dbname="rag_pipeline",
        user="lagnashatripathy",
        host="localhost",
        port="5432"
    )

    from pgvector.psycopg2 import register_vector
    register_vector(conn)

    cur = conn.cursor()

    for i, chunk in enumerate(chunks, start=1):
        print(f"Embedding chunk {i}/{len(chunks)}...")
        vector = get_embedding(chunk["text"])

        if i == 1:
            print(f"Embedding dimension: {len(vector)}")  # should print 768

        cur.execute(
            """
            INSERT INTO rag_chunks (text, embedding)
            VALUES (%s, %s)
            """,
            (chunk["text"], vector)
        )

    conn.commit()
    cur.close()
    conn.close()
    print("\n✅ All embeddings stored successfully.")

# ============================================================
# 6. MAIN PIPELINE
# ============================================================

if __name__ == "__main__":
    data_path = Path(__file__).parent.parent / "data" / "txt"

    documents = load_documents(data_path)
    print("Documents loaded:", len(documents))

    chunks = create_chunks(documents)
    print("Chunks created:", len(chunks))

    store_embeddings(chunks)
