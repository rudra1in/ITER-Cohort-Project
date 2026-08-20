# ============================================================
# PROBLEM MODEL
# ============================================================

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
)

from sqlalchemy.dialects.postgresql import ARRAY

from app.database.database import Base


class Problem(Base):

    __tablename__ = "problems"

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
        unique=True,
        nullable=False,
        index=True,
    )

    # --------------------------------------------------------
    # Title
    # --------------------------------------------------------

    title = Column(
        String(255),
        nullable=False,
    )

    # --------------------------------------------------------
    # Difficulty
    # --------------------------------------------------------

    difficulty = Column(
        String(50),
        nullable=True,
    )

    # --------------------------------------------------------
    # Main Topic
    # --------------------------------------------------------

    topic = Column(
        String(100),
        nullable=True,
        index=True,
    )

    # --------------------------------------------------------
    # Pattern
    # --------------------------------------------------------

    pattern = Column(
        String(255),
        nullable=True,
    )

    # --------------------------------------------------------
    # Additional Topics
    # --------------------------------------------------------

    topics = Column(
        ARRAY(Text),
        nullable=True,
    )