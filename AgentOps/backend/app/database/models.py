from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

from pgvector.sqlalchemy import Vector

from app.database.database import Base


class KnowledgeChunk(Base):
    __tablename__ = "knowledge_chunks"

    id = Column(Integer, primary_key=True, index=True)

    problem_id = Column(
        String(255),
        nullable=False,
        index=True,
    )

    title = Column(
        String(255),
        nullable=False,
    )

    topic = Column(
        String(100),
        nullable=True,
        index=True,
    )

    difficulty = Column(
        String(50),
        nullable=True,
    )

    pattern = Column(
        String(255),
        nullable=True,
    )

    section = Column(
        String(255),
        nullable=True,
    )

    content = Column(
        Text,
        nullable=False,
    )

    source = Column(
        Text,
        nullable=True,
    )

    embedding = Column(
        Vector(384),
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )