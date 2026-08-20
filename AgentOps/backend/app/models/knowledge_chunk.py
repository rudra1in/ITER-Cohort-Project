# ============================================================
# KNOWLEDGE CHUNK MODEL
# PostgreSQL + pgvector
# ============================================================

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Index,
)

from pgvector.sqlalchemy import Vector

from app.database.database import Base


# ============================================================
# CONFIGURATION
# ============================================================

EMBEDDING_DIMENSION = 384


# ============================================================
# KNOWLEDGE CHUNK
# ============================================================

class KnowledgeChunk(Base):

    __tablename__ = "knowledge_chunks"

    # --------------------------------------------------------
    # Primary Key
    # --------------------------------------------------------

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    # --------------------------------------------------------
    # Problem ID
    # --------------------------------------------------------

    problem_id = Column(
        String(255),
        nullable=False,
        index=True,
    )

    # --------------------------------------------------------
    # Section
    # --------------------------------------------------------

    section = Column(
        String(255),
        nullable=False,
        index=True,
    )

    # --------------------------------------------------------
    # Section Title
    # --------------------------------------------------------

    section_title = Column(
        String(255),
        nullable=True,
    )

    # --------------------------------------------------------
    # Chunk Index
    # --------------------------------------------------------

    chunk_index = Column(
        Integer,
        nullable=False,
    )

    # --------------------------------------------------------
    # Content
    # --------------------------------------------------------

    content = Column(
        Text,
        nullable=False,
    )

    # --------------------------------------------------------
    # Source Markdown File
    # --------------------------------------------------------

    source = Column(
        Text,
        nullable=True,
    )

    # --------------------------------------------------------
    # Embedding
    # --------------------------------------------------------

    embedding = Column(
        Vector(EMBEDDING_DIMENSION),
        nullable=False,
    )


# ============================================================
# INDEXES
# ============================================================

Index(
    "ix_knowledge_chunks_problem_section",
    KnowledgeChunk.problem_id,
    KnowledgeChunk.section,
)