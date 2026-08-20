# ============================================================
# TEST VECTOR STORE
# PostgreSQL + pgvector
# ============================================================

from sqlalchemy import text

from app.database.database import SessionLocal


# ============================================================
# DATABASE CONNECTION TEST
# ============================================================

def test_database_connection():

    db = SessionLocal()

    try:

        result = db.execute(
            text("SELECT 1")
        ).scalar()

        print()
        print("========== DATABASE TEST ==========")

        if result == 1:

            print(
                "PostgreSQL connection: OK"
            )

        else:

            print(
                "PostgreSQL connection: FAILED"
            )

    finally:

        db.close()


# ============================================================
# PGVECTOR TEST
# ============================================================

def test_pgvector():

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

        print()
        print("========== PGVECTOR TEST ==========")

        if result == "vector":

            print(
                "pgvector extension: OK"
            )

        else:

            print(
                "pgvector extension: NOT FOUND"
            )

    finally:

        db.close()


# ============================================================
# KNOWLEDGE CHUNK TABLE TEST
# ============================================================

def test_knowledge_chunks():

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

        print()
        print(
            "========== KNOWLEDGE CHUNKS TEST =========="
        )

        print(
            f"Stored knowledge chunks: {result}"
        )

    finally:

        db.close()


# ============================================================
# EMBEDDING TEST
# ============================================================

# ============================================================
# EMBEDDING TEST
# ============================================================

def test_embeddings():

    db = SessionLocal()

    try:

        row = db.execute(
            text(
                """
                SELECT
                    id,
                    problem_id,
                    title,
                    topic,
                    difficulty,
                    pattern,
                    section,
                    embedding
                FROM knowledge_chunks
                WHERE embedding IS NOT NULL
                LIMIT 1
                """
            )
        ).fetchone()

        print()
        print(
            "========== EMBEDDING TEST =========="
        )

        if row is None:

            print(
                "No embeddings found."
            )

            return

        print(
            f"ID: {row.id}"
        )

        print(
            f"Problem ID: {row.problem_id}"
        )

        print(
            f"Title: {row.title}"
        )

        print(
            f"Topic: {row.topic}"
        )

        print(
            f"Difficulty: {row.difficulty}"
        )

        print(
            f"Pattern: {row.pattern}"
        )

        print(
            f"Section: {row.section}"
        )

        embedding = row.embedding

        print(
            f"Embedding dimension: {len(embedding)}"
        )

        print(
            "First 10 values:"
        )

        print(
            embedding[:10]
        )

    finally:

        db.close()


# ============================================================
# PGVECTOR SIMILARITY TEST
# ============================================================

def test_similarity_search():

    db = SessionLocal()

    try:

        # This is only a technical pgvector test.
        # It is NOT testing semantic relevance.
        #
        # IMPORTANT:
        # The actual embedding dimension in the database
        # is currently 4710, so the test vector must also
        # contain 4710 values.

        test_vector = [0.0] * 384

        rows = db.execute(
            text(
                """
                SELECT
                    id,
                    problem_id,
                    section,

                    embedding <=> CAST(
                        :query_embedding AS vector
                    ) AS distance

                FROM knowledge_chunks

                WHERE embedding IS NOT NULL

                ORDER BY
                    embedding <=> CAST(
                        :query_embedding AS vector
                    )

                LIMIT 5
                """
            ),
            {
                "query_embedding": str(
                    test_vector
                )
            },
        ).fetchall()

        print()
        print(
            "========== VECTOR SEARCH TEST =========="
        )

        print(
            f"Retrieved {len(rows)} chunks using pgvector."
        )

        for index, row in enumerate(
            rows,
            start=1,
        ):

            print()
            print(
                f"----------- Result {index} -----------"
            )

            print(
                f"Problem ID: {row.problem_id}"
            )

            print(
                f"Section: {row.section}"
            )

            print(
                f"Distance: {row.distance}"
            )

    finally:

        db.close()


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    print()
    print("==============================================")
    print(" POSTGRESQL + PGVECTOR VECTOR STORE TEST")
    print("==============================================")

    test_database_connection()

    test_pgvector()

    test_knowledge_chunks()

    test_embeddings()

    test_similarity_search()

    print()
    print("==============================================")
    print(" VECTOR STORE TEST COMPLETE")
    print("==============================================")