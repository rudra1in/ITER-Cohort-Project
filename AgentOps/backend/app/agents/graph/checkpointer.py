import os

from dotenv import load_dotenv
from psycopg import Connection
from langgraph.checkpoint.postgres import PostgresSaver


load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")


if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL is not configured in the .env file."
    )


PSYCOPG_DATABASE_URL = DATABASE_URL.replace(
    "postgresql+psycopg://",
    "postgresql://",
)


def create_checkpointer():
    """
    Create the PostgreSQL checkpointer used by LangGraph.

    LangGraph uses this checkpointer to persist graph state
    and conversation memory in PostgreSQL.
    """

    connection = Connection.connect(
        PSYCOPG_DATABASE_URL,
        autocommit=True,
    )

    checkpointer = PostgresSaver(connection)

    checkpointer.setup()

    return checkpointer