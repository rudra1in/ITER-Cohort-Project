from sqlalchemy import text

from app.databse.database import Base, engine

# Import models so SQLAlchemy registers them.
from app.models import Problem, KnowledgeChunk


def initialize_database():
    """
    Create the pgvector extension and application tables.
    """

    with engine.begin() as connection:

        connection.execute(
            text(
                "CREATE EXTENSION IF NOT EXISTS vector"
            )
        )

    Base.metadata.create_all(
        bind=engine
    )

    print("Database initialized successfully.")