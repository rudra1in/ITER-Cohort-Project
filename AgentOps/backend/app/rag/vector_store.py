# ============================================================
# VECTOR STORE
# PostgreSQL + pgvector
# ============================================================

from sqlalchemy import text

from app.database.database import SessionLocal


# ============================================================
# CONFIGURATION
# ============================================================

EMBEDDING_DIMENSION = 384

TABLE_NAME = "knowledge_chunks"


# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_vector_store_session():
    """
    Return a SQLAlchemy database session.

    PostgreSQL is the actual vector store.
    pgvector stores and searches the embeddings.
    """

    return SessionLocal()


# ============================================================
# CHECK PGVECTOR
# ============================================================

def check_pgvector():
    """
    Check whether the pgvector extension
    is installed in PostgreSQL.
    """

    db = SessionLocal()

    try:

        result = db.execute(
            text(
                """
                SELECT extname
                FROM pg_extension
                WHERE extname = 'vector'
                """
            )
        ).scalar()

        return result == "vector"

    finally:

        db.close()


# ============================================================
# COUNT STORED CHUNKS
# ============================================================

def get_chunk_count():
    """
    Return the total number of knowledge chunks
    stored in PostgreSQL.
    """

    db = SessionLocal()

    try:

        result = db.execute(
            text(
                """
                SELECT COUNT(*)
                FROM knowledge_chunks
                """
            )
        ).scalar()

        return result or 0

    finally:

        db.close()


# ============================================================
# COUNT EMBEDDED CHUNKS
# ============================================================

def get_embedded_chunk_count():
    """
    Return the number of chunks that have
    a non-null embedding.
    """

    db = SessionLocal()

    try:

        result = db.execute(
            text(
                """
                SELECT COUNT(*)
                FROM knowledge_chunks
                WHERE embedding IS NOT NULL
                """
            )
        ).scalar()

        return result or 0

    finally:

        db.close()


# ============================================================
# VECTOR SIMILARITY SEARCH
# ============================================================

def similarity_search(
    query_embedding,
    limit=5,
):
    """
    Perform vector similarity search using pgvector.

    `<=>` is pgvector's cosine distance operator.

    Smaller distance = more similar vector.
    """

    if not query_embedding:
        return []

    if len(query_embedding) != EMBEDDING_DIMENSION:
        raise ValueError(
            f"Expected embedding dimension "
            f"{EMBEDDING_DIMENSION}, "
            f"received {len(query_embedding)}."
        )

    db = SessionLocal()

    try:

        rows = db.execute(
            text(
                """
                SELECT
                    id,
                    problem_id,
                    section,
                    section_title,
                    chunk_index,
                    content,
                    source,

                    embedding <=> CAST(
                        :query_embedding AS vector
                    ) AS distance

                FROM knowledge_chunks

                WHERE embedding IS NOT NULL

                ORDER BY
                    embedding <=> CAST(
                        :query_embedding AS vector
                    )

                LIMIT :limit
                """
            ),
            {
                "query_embedding": str(
                    query_embedding
                ),
                "limit": int(limit),
            },
        ).fetchall()

        return rows

    finally:

        db.close()


# ============================================================
# VECTOR STORE INFORMATION
# ============================================================

def get_vector_store_info():

    return {
        "database": "PostgreSQL",
        "vector_extension": "pgvector",
        "table": TABLE_NAME,
        "embedding_dimension": EMBEDDING_DIMENSION,
        "similarity_metric": "cosine distance",
    }


# ============================================================
# MANUAL TEST
# ============================================================

if __name__ == "__main__":

    print()
    print("==============================================")
    print(" POSTGRESQL + PGVECTOR VECTOR STORE")
    print("==============================================")

    print()
    print("Vector store information:")

    info = get_vector_store_info()

    for key, value in info.items():

        print(
            f"{key}: {value}"
        )

    print()
    print("Checking pgvector...")

    if check_pgvector():

        print(
            "pgvector extension: OK"
        )

    else:

        print(
            "pgvector extension: NOT FOUND"
        )

    print()
    print("Checking knowledge chunks...")

    try:

        total = get_chunk_count()

        embedded = get_embedded_chunk_count()

        print(
            f"Total chunks: {total}"
        )

        print(
            f"Chunks with embeddings: {embedded}"
        )

    except Exception as error:

        print(
            f"Database error: {error}"
        )