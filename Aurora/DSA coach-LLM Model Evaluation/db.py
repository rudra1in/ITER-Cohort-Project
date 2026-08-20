# db.py
import os
import csv
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables
load_dotenv("apikeys.env")

DATABASE_URL = os.getenv("DATABASE_URL")

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, isolation_level="AUTOCOMMIT")

def init_db():
    with engine.connect() as conn:
        # Enable pgvector extension
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))

        # Table 1: Raw text chunks
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS raw_documents (
                id SERIAL PRIMARY KEY,
                filename TEXT,
                chunk_id INT,
                content TEXT
            );
        """))

        # Table 2: Embeddings linked to raw_documents
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS document_embeddings (
                id SERIAL PRIMARY KEY,
                raw_id INT,
                embedding VECTOR(1536),
                FOREIGN KEY (raw_id) REFERENCES raw_documents(id)
            );
        """))

        print("✅ dsacoachdb initialized with raw_documents and document_embeddings tables.")

def export_to_files(raw_data, embeddings):
    """
    raw_data: list of dicts with keys [filename, chunk_id, content]
    embeddings: list of dicts with keys [chunk_id, embedding]
    """
    os.makedirs("data_store", exist_ok=True)

    # Write raw chunks to CSV
    with open("data_store/chunks.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["filename", "chunk_id", "content"])
        writer.writeheader()
        writer.writerows(raw_data)

    # Write embeddings to CSV
    with open("data_store/embeddings.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["chunk_id", "embedding"])
        writer.writeheader()
        writer.writerows(embeddings)

    print("📂 Exported chunks.csv and embeddings.csv to data_store/")