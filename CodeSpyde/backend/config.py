import os
from pathlib import Path

from dotenv import load_dotenv


# ---------------------------------------------------------
# Project paths
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent

load_dotenv(BASE_DIR / ".env")


# ---------------------------------------------------------
# Environment helpers
# ---------------------------------------------------------

def get_required_env(name: str) -> str:
    value = os.getenv(name)

    if not value:
        raise RuntimeError(
            f"Required environment variable '{name}' is not set."
        )

    return value


# ---------------------------------------------------------
# Application
# ---------------------------------------------------------

APP_NAME = os.getenv(
    "APP_NAME",
    "AI DSA Coach"
)

APP_VERSION = os.getenv(
    "APP_VERSION",
    "1.0.0"
)

DEBUG = os.getenv(
    "DEBUG",
    "true"
).lower() == "true"


# ---------------------------------------------------------
# Database
# ---------------------------------------------------------

DATABASE_URL = os.getenv(
    "DATABASE_URL"
)


# ---------------------------------------------------------
# Gemini
# ---------------------------------------------------------

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

# Keep model names configurable instead of hard-coding them.
# You can change them in .env without modifying Python code.

GEMINI_COACH_MODEL = os.getenv(
    "GEMINI_COACH_MODEL"
)

GEMINI_DEBUGGER_MODEL = os.getenv(
    "GEMINI_DEBUGGER_MODEL"
)

GEMINI_FAST_MODEL = os.getenv(
    "GEMINI_FAST_MODEL"
)

GEMINI_EMBEDDING_MODEL = os.getenv(
    "GEMINI_EMBEDDING_MODEL"
)


# ---------------------------------------------------------
# Code execution
# ---------------------------------------------------------

PYTHON_EXECUTABLE = os.getenv(
    "PYTHON_EXECUTABLE",
    "python"
)

CODE_EXECUTION_TIMEOUT = int(
    os.getenv(
        "CODE_EXECUTION_TIMEOUT",
        "3"
    )
)

MAX_OUTPUT_LENGTH = int(
    os.getenv(
        "MAX_OUTPUT_LENGTH",
        "10000"
    )
)


# ---------------------------------------------------------
# RAG
# ---------------------------------------------------------

EMBEDDING_DIMENSION = int(
    os.getenv(
        "EMBEDDING_DIMENSION",
        "768"
    )
)

VECTOR_SEARCH_LIMIT = int(
    os.getenv(
        "VECTOR_SEARCH_LIMIT",
        "15"
    )
)

FINAL_CONTEXT_LIMIT = int(
    os.getenv(
        "FINAL_CONTEXT_LIMIT",
        "7"
    )
)

# ---------------------------------------------------------
# Retrieval
# ---------------------------------------------------------

VECTOR_SEARCH_LIMIT = int(
    os.getenv(
        "VECTOR_SEARCH_LIMIT",
        "20"
    )
)

KEYWORD_SEARCH_LIMIT = int(
    os.getenv(
        "KEYWORD_SEARCH_LIMIT",
        "20"
    )
)

HYBRID_SEARCH_LIMIT = int(
    os.getenv(
        "HYBRID_SEARCH_LIMIT",
        "15"
    )
)

RERANK_LIMIT = int(
    os.getenv(
        "RERANK_LIMIT",
        "8"
    )
)

FINAL_CONTEXT_LIMIT = int(
    os.getenv(
        "FINAL_CONTEXT_LIMIT",
        "6"
    )
)


# ---------------------------------------------------------
# Reranker
# ---------------------------------------------------------

RERANKER_MODEL = os.getenv(
    "RERANKER_MODEL",
    "BAAI/bge-reranker-v2-m3"
)

RERANKER_ENABLED = (
    os.getenv(
        "RERANKER_ENABLED",
        "true"
    ).lower()
    == "true"
)