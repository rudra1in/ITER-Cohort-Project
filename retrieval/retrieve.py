
import os

OLLAMA_MODEL = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")


def get_query_embedding(query_text):
    """
    Generate an embedding with Ollama.
    Import is kept inside the function so the Streamlit UI can still start
    when Ollama is not installed/configured.
    """
    from ollama import Client

    client = Client(
        host=os.getenv("OLLAMA_HOST", "http://localhost:11434")
    )

    response = client.embeddings(
        model=OLLAMA_MODEL,
        prompt=query_text,
    )
    return response["embedding"]


def retrieve_chunks(query_text, top_k=5):
    """
    Optional PostgreSQL + pgvector RAG retrieval.
    Returns [] if the database is unavailable.
    """
    try:
        import psycopg2
        from pgvector.psycopg2 import register_vector

        conn = psycopg2.connect(
            dbname=os.getenv("PGDATABASE", "rag_pipeline"),
            user=os.getenv("PGUSER", ""),
            password=os.getenv("PGPASSWORD", ""),
            host=os.getenv("PGHOST", "localhost"),
            port=os.getenv("PGPORT", "5432"),
        )

        register_vector(conn)

        embedding = get_query_embedding(query_text)

        cur = conn.cursor()
        cur.execute(
            """
            SELECT text, embedding <-> %s::vector AS distance
            FROM rag_chunks
            ORDER BY embedding <-> %s::vector
            LIMIT %s;
            """,
            (embedding, embedding, top_k),
        )

        rows = cur.fetchall()

        cur.close()
        conn.close()

        return [
            {"text": row[0], "distance": row[1]}
            for row in rows
        ]

    except Exception as exc:
        print(f"[RAG] unavailable: {exc}")
        return []
