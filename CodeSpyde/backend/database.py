from contextlib import contextmanager

import psycopg2
from psycopg2.extras import RealDictCursor
from pgvector.psycopg2 import register_vector

from config import DATABASE_URL


if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL is not configured."
    )


def _configure_connection(connection):
    """
    Configure PostgreSQL connection for pgvector.
    """

    try:
        register_vector(connection)
    except Exception:
        pass

    return connection


@contextmanager
def get_db_connection():
    """
    Create and safely close a PostgreSQL connection.
    """

    connection = None

    try:

        connection = psycopg2.connect(
            DATABASE_URL
        )

        _configure_connection(
            connection
        )

        yield connection

    except Exception:

        if connection:
            connection.rollback()

        raise

    finally:

        if connection:
            connection.close()


@contextmanager
def get_db_cursor(
    dict_cursor: bool = False
):
    """
    Create a database cursor and automatically
    handle commit/rollback.
    """

    cursor = None

    with get_db_connection() as connection:

        try:

            cursor_factory = (
                RealDictCursor
                if dict_cursor
                else None
            )

            cursor = connection.cursor(
                cursor_factory=cursor_factory
            )

            yield cursor

            connection.commit()

        except Exception:

            connection.rollback()

            raise

        finally:

            if cursor:
                cursor.close()


def execute_sql(
    sql: str,
    params=None
):
    """
    Execute a SQL statement.
    """

    with get_db_cursor() as cursor:

        cursor.execute(
            sql,
            params
        )