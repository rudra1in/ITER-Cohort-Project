import os
from dotenv import load_dotenv


load_dotenv()


# =========================================================
# DIRECTORIES
# =========================================================

DATA_DIR = os.getenv(
    "DATA_DIR",
    "data"
)

RAW_DIR = os.getenv(
    "RAW_DIR",
    "data/raw"
)

PROCESSED_DIR = os.getenv(
    "PROCESSED_DIR",
    "data/processed"
)

REPORT_DIR = os.getenv(
    "REPORT_DIR",
    "data/reports"
)

DATABASE_PATH = os.getenv(
    "DATABASE_PATH",
    "data/app.db"
)


# =========================================================
# YOLO
# =========================================================

YOLO_MODEL = os.getenv(
    "YOLO_MODEL",
    "yolo11n.pt"
)

YOLO_POSE_MODEL = os.getenv(
    "YOLO_POSE_MODEL",
    "yolo11n-pose.pt"
)


TRACK_CONFIDENCE = float(
    os.getenv(
        "TRACK_CONFIDENCE",
        "0.35"
    )
)

POSE_CONFIDENCE = float(
    os.getenv(
        "POSE_CONFIDENCE",
        "0.35"
    )
)


# =========================================================
# IMAGE FILTERING
# =========================================================

PHASH_THRESHOLD = int(
    os.getenv(
        "PHASH_THRESHOLD",
        "8"
    )
)

CHANGE_THRESHOLD = float(
    os.getenv(
        "CHANGE_THRESHOLD",
        "0.08"
    )
)

MIN_IMAGE_WIDTH = int(
    os.getenv(
        "MIN_IMAGE_WIDTH",
        "320"
    )
)

MIN_IMAGE_HEIGHT = int(
    os.getenv(
        "MIN_IMAGE_HEIGHT",
        "240"
    )
)


# =========================================================
# BEHAVIOR
# =========================================================

LOOK_LEFT_THRESHOLD = float(
    os.getenv(
        "LOOK_LEFT_THRESHOLD",
        "-15"
    )
)

LOOK_RIGHT_THRESHOLD = float(
    os.getenv(
        "LOOK_RIGHT_THRESHOLD",
        "15"
    )
)

MIN_EVENT_DURATION = float(
    os.getenv(
        "MIN_EVENT_DURATION",
        "3"
    )
)

EVENT_GAP_SECONDS = float(
    os.getenv(
        "EVENT_GAP_SECONDS",
        "3"
    )
)


# =========================================================
# FILES
# =========================================================

SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp"
}


# =========================================================
# DIRECTORIES
# =========================================================

for directory in [
    DATA_DIR,
    RAW_DIR,
    PROCESSED_DIR,
    REPORT_DIR
]:

    os.makedirs(
        directory,
        exist_ok=True
    )
# =========================================================
# EMBEDDING / RAG
# =========================================================

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-MiniLM-L6-v2"
)

VECTOR_DIR = os.getenv(
    "VECTOR_DIR",
    "data/vector_store"
)



# =========================================================
# LLM (dual provider: Gemini API or local Ollama)
# =========================================================

LLM_PROVIDER = os.getenv(
    "LLM_PROVIDER",
    "gemini"
)

LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "gemini-3.6-flash"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.2:1b"
)

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434"
)
# =========================================================
# RAG & MEMORY
# =========================================================

RAG_TOP_K = int(
    os.getenv(
        "RAG_TOP_K",
        "8"
    )
)

RAG_FINAL_K = int(
    os.getenv(
        "RAG_FINAL_K",
        "5"
    )
)

MEMORY_LIMIT = int(
    os.getenv(
        "MEMORY_LIMIT",
        "8"
    )
)


# =========================================================
# GEMINI ESCALATION (optional failsafe for ambiguous frames)
# =========================================================

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY",
    None
)

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.6-flash"
)

GEMINI_CONFIDENCE_THRESHOLD = float(
    os.getenv(
        "GEMINI_CONFIDENCE_THRESHOLD",
        "0.3"
    )
)


# =========================================================
# MEDIAPIPE FACE REFINEMENT (optional)
# =========================================================

FACE_LANDMARKER_MODEL_PATH = os.getenv(
    "FACE_LANDMARKER_MODEL_PATH",
    "models/face_landmarker.task"
)