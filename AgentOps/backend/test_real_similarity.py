from sqlalchemy import text

from app.database.database import SessionLocal
from app.rag.embeddings import create_embedding_model


print("Creating embedding model...")

embedding_model = create_embedding_model()

query = "How do I find the maximum element in an array?"

print("Creating query embedding...")

query_embedding = embedding_model.embed_query(query)

print("Query embedding dimension:", len(query_embedding))


db = SessionLocal()

try:

    rows = db.execute(
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
                content,

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
            "query_embedding": str(query_embedding),
        },
    ).fetchall()

    print()
    print("========== REAL VECTOR SEARCH ==========")
    print(f"Retrieved {len(rows)} chunks.")

    for index, row in enumerate(rows, start=1):

        print()
        print(f"----------- Result {index} -----------")
        print("Problem ID:", row.problem_id)
        print("Title:", row.title)
        print("Topic:", row.topic)
        print("Difficulty:", row.difficulty)
        print("Pattern:", row.pattern)
        print("Section:", row.section)
        print("Distance:", row.distance)
        print("Content:")
        print(row.content)

finally:

    db.close()