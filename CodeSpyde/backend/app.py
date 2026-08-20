from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import (
    APP_NAME,
    APP_VERSION,
    DEBUG
)

from routes.code import (
    router as code_router
)

from routes.problems import (
    router as problems_router
)

from routes.rag import (
    router as rag_router
)

from routes.coach import (
    router as coach_router
)


app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    debug=DEBUG
)


# =========================================================
# DATABASE SCHEMA INIT (idempotent)
# =========================================================

@app.on_event("startup")
async def init_database():
    """
    Run schema.sql at startup.
    The SQL uses IF NOT EXISTS / DO NOTHING guards so this
    is safe to run on every boot.
    """
    import logging
    from pathlib import Path
    from database import get_db_cursor

    logger = logging.getLogger(__name__)

    schema_path = (
        Path(__file__).resolve().parent
        / "sql"
        / "schema.sql"
    )

    if not schema_path.exists():
        logger.warning(
            "schema.sql not found at %s — "
            "skipping DB init.",
            schema_path,
        )
        return

    try:
        sql = schema_path.read_text(
            encoding="utf-8"
        )

        with get_db_cursor() as cursor:
            cursor.execute(sql)

        logger.info(
            "Database schema initialized."
        )
    except Exception as exc:
        logger.error(
            "Database init failed: %s",
            exc,
        )


# =========================================================
# CORS
# =========================================================

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)


# =========================================================
# ROUTES
# =========================================================

app.include_router(
    code_router
)

app.include_router(
    problems_router
)

app.include_router(
    rag_router
)

app.include_router(
    coach_router
)


# =========================================================
# HEALTH
# =========================================================

@app.get("/")
async def root():

    return {
        "service": APP_NAME,

        "version": APP_VERSION,

        "status": "running"
    }


@app.get("/health")
async def health():

    return {
        "status": "healthy"
    }