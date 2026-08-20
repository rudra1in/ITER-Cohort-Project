from sqlalchemy import text
from app.database.database import SessionLocal


db = SessionLocal()

try:
    rows = db.execute(
        text(
            """
            SELECT
                column_name,
                data_type
            FROM information_schema.columns
            WHERE table_name = 'knowledge_chunks'
            ORDER BY ordinal_position
            """
        )
    ).fetchall()

    print()
    print("========== KNOWLEDGE_CHUNKS SCHEMA ==========")

    for row in rows:
        print(f"{row[0]} -> {row[1]}")

finally:
    db.close()