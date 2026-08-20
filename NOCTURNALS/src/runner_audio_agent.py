# ============================================================
# FILE: src/runner_audio_agent.py
# ============================================================

import argparse
import json
import sys
import uuid
from pathlib import Path
from typing import Any, Dict

# ============================================================
# PROJECT ROOT
# ============================================================

PROJECT_ROOT = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

if str(
    PROJECT_ROOT
) not in sys.path:

    sys.path.insert(
        0,
        str(PROJECT_ROOT),
    )


# ============================================================
# PROJECT IMPORTS
# ============================================================

from src.audio.validator import (
    validate_audio,
)

from src.audio.preprocess import (
    preprocess_audio,
)

from src.audio.chunker import (
    chunk_audio,
)

from src.audio.analyzer import (
    analyze_audio_chunk,
)

from src.agent.graph import (
    AudioReActGraph,
)

from src.agent.ollama_reasoner import (
    OllamaReasoner,
)

from src.rag.store import (
    AudioRAGStore,
)


# ============================================================
# CONFIGURATION
# ============================================================

MAX_REACT_STEPS = 3

LOW_CONFIDENCE_THRESHOLD = 0.60

HIGH_CONFIDENCE_THRESHOLD = 0.80

OLLAMA_MODEL = "qwen3:8b"

OLLAMA_BASE_URL = (
    "http://localhost:11434"
)

OLLAMA_TIMEOUT = 90

OLLAMA_MAX_RETRIES = 2

EMBEDDING_MODEL = (
    "nomic-embed-text"
)

CHUNK_SECONDS = 5.0

OVERLAP_SECONDS = 1.0

SEMANTIC_TOP_K = 5


# ============================================================
# AUDIO ID
# ============================================================

def generate_audio_id() -> str:

    return (
        f"audio_"
        f"{uuid.uuid4().hex[:10]}"
    )


# ============================================================
# REPORT
# ============================================================

def generate_report(
    final_state: dict,
    audio_file_id: str,
    source_file: str,
    student_id: str,
) -> Path:

    report_directory = (
        PROJECT_ROOT
        / "data"
        / "audio_reports"
    )

    report_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    report_path = (
        report_directory
        / (
            f"{audio_file_id}"
            "_report.json"
        )
    )

    results = final_state.get(
        "report_results",
        [],
    )

    review_count = sum(
        1
        for result in results
        if bool(
            result.get(
                "review_required",
                False,
            )
        )
    )

    context_count = sum(
        1
        for result in results
        if bool(
            result.get(
                "context_used",
                False,
            )
        )
    )

    reanalysis_count = sum(
        1
        for result in results
        if bool(
            result.get(
                "reanalyzed",
                False,
            )
        )
    )

    label_summary = {}

    for result in results:

        label = str(
            result.get(
                "assigned_label",
                "OTHER",
            )
        )

        label_summary[label] = (
            label_summary.get(
                label,
                0,
            )
            + 1
        )

    report = {
        "project": (
            "Local Audio Detection "
            "ReAct Agent with "
            "Student-Scoped Semantic RAG"
        ),

        "student_id": student_id,

        "audio_file_id": (
            audio_file_id
        ),

        "source_file": (
            str(source_file)
        ),

        "configuration": {
            "max_react_steps": (
                MAX_REACT_STEPS
            ),

            "low_confidence_threshold": (
                LOW_CONFIDENCE_THRESHOLD
            ),

            "high_confidence_threshold": (
                HIGH_CONFIDENCE_THRESHOLD
            ),

            "ollama_model": (
                OLLAMA_MODEL
            ),

            "embedding_model": (
                EMBEDDING_MODEL
            ),

            "ollama_timeout": (
                OLLAMA_TIMEOUT
            ),

            "chunk_seconds": (
                CHUNK_SECONDS
            ),

            "overlap_seconds": (
                OVERLAP_SECONDS
            ),

            "semantic_top_k": (
                SEMANTIC_TOP_K
            ),
        },

        "chunks_processed": (
            len(results)
        ),

        "review_required": (
            review_count
        ),

        "chunks_with_semantic_context": (
            context_count
        ),

        "chunks_reanalyzed": (
            reanalysis_count
        ),

        "label_summary": (
            label_summary
        ),

        "results": results,
    }

    with open(
        report_path,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            report,
            file,
            indent=2,
            ensure_ascii=False,
        )

    return report_path


# ============================================================
# MAIN
# ============================================================

def main():

    parser = argparse.ArgumentParser(
        description=(
            "Local Audio Detection "
            "ReAct Agent with "
            "Student-Scoped Semantic RAG"
        )
    )

    parser.add_argument(
        "--audio",
        required=True,
        help=(
            "Path to input audio file."
        ),
    )

    parser.add_argument(
        "--student-id",
        required=True,
        help=(
            "Student identifier used to "
            "scope historical semantic "
            "retrieval."
        ),
    )

    args = parser.parse_args()

    # ========================================================
    # RESOLVE AUDIO
    # ========================================================

    audio_path = (
        Path(
            args.audio
        )
        .expanduser()
        .resolve()
    )

    student_id = (
        str(
            args.student_id
        ).strip()
    )

    if not student_id:

        print(
            "[ERROR] Student ID "
            "cannot be empty."
        )

        sys.exit(1)

    if not audio_path.exists():

        print(
            "[ERROR] Audio file "
            "does not exist:"
        )

        print(
            audio_path
        )

        sys.exit(1)

    # ========================================================
    # HEADER
    # ========================================================

    print()

    print(
        "================================================"
    )

    print(
        " LOCAL AUDIO DETECTION REACT AGENT"
    )

    print(
        " STUDENT-SCOPED SEMANTIC RAG"
    )

    print(
        "================================================"
    )

    print(
        f"Input:      {audio_path}"
    )

    print(
        f"Student ID: {student_id}"
    )

    # ========================================================
    # AUDIO ID
    # ========================================================

    audio_file_id = (
        generate_audio_id()
    )

    print(
        f"Audio ID:   {audio_file_id}"
    )

    # ========================================================
    # STEP 1 — VALIDATE
    # ========================================================

    print()
    print(
        "[1/5] Validating audio..."
    )

    try:

        validation = (
            validate_audio(
                str(audio_path)
            )
        )

    except Exception as exc:

        print(
            "[ERROR] Audio validation failed:"
        )

        print(
            exc
        )

        sys.exit(1)

    duration = float(
        validation[
            "duration"
        ]
    )

    print(
        f"[1/5] Validated: "
        f"{duration:.2f}s"
    )

    # ========================================================
    # STEP 1 — PREPROCESS
    # ========================================================

    processed_directory = (
        PROJECT_ROOT
        / "data"
        / "processed_audio"
    )

    processed_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    processed_audio_path = (
        processed_directory
        / (
            f"{audio_file_id}.wav"
        )
    )

    print(
        "[1/5] Preprocessing..."
    )

    try:

        preprocess_audio(
            input_path=str(
                audio_path
            ),
            output_path=str(
                processed_audio_path
            ),
        )

    except Exception as exc:

        print(
            "[ERROR] Preprocessing failed:"
        )

        print(
            exc
        )

        sys.exit(1)

    print(
        "[1/5] Preprocessed: "
        "mono / 16kHz WAV"
    )

    # ========================================================
    # STEP 2 — CHUNK
    # ========================================================

    chunk_directory = (
        PROJECT_ROOT
        / "data"
        / "audio_chunks"
        / audio_file_id
    )

    chunk_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    print(
        "[2/5] Creating chunks..."
    )

    try:

        chunks = chunk_audio(
            wav_path=str(
                processed_audio_path
            ),
            output_dir=str(
                chunk_directory
            ),
            chunk_seconds=(
                CHUNK_SECONDS
            ),
            overlap_seconds=(
                OVERLAP_SECONDS
            ),
        )

    except Exception as exc:

        print(
            "[ERROR] Chunking failed:"
        )

        print(
            exc
        )

        sys.exit(1)

    if not chunks:

        print(
            "[ERROR] No chunks created."
        )

        sys.exit(1)

    print(
        f"[2/5] Created "
        f"{len(chunks)} chunks "
        f"({CHUNK_SECONDS:.1f}s "
        f"windows, "
        f"{OVERLAP_SECONDS:.1f}s "
        f"overlap)"
    )

    # ========================================================
    # STEP 2.5 — INITIAL ANALYSIS CACHE
    # ========================================================

    print()
    print(
        "[2/5] Building initial "
        "analysis cache..."
    )

    precomputed_analyses: Dict[
        str,
        Dict[str, Any],
    ] = {}

    try:

        for index, chunk in enumerate(
            chunks,
            start=1,
        ):

            chunk_id = str(
                chunk[
                    "chunk_id"
                ]
            )

            analysis = (
                analyze_audio_chunk(
                    chunk[
                        "storage_path"
                    ]
                )
            )

            precomputed_analyses[
                chunk_id
            ] = analysis

            print(
                f"  [Audio] "
                f"{index}/"
                f"{len(chunks)} "
                f"{chunk_id} -> "
                f"{analysis.get('event')} "
                f"("
                f"{float(analysis.get('confidence', 0.0)):.3f}"
                f")"
            )

    except Exception as exc:

        print(
            "[ERROR] Initial analysis failed:"
        )

        print(
            exc
        )

        sys.exit(1)

    # ========================================================
    # STEP 3 — CHROMADB + EMBEDDINGS
    # ========================================================

    print()
    print(
        "[3/5] Initializing "
        "semantic RAG..."
    )

    try:

        rag_store = AudioRAGStore(
            ollama_base_url=(
                OLLAMA_BASE_URL
            ),
            embedding_model=(
                EMBEDDING_MODEL
            ),
        )

    except Exception as exc:

        print(
            "[ERROR] RAG initialization failed:"
        )

        print(
            exc
        )

        sys.exit(1)

    print(
        "[3/5] ChromaDB ready"
    )

    print(
        f"[3/5] Embedding model: "
        f"{EMBEDDING_MODEL}"
    )

    # ========================================================
    # STUDENT HISTORY STATISTICS
    # ========================================================

    historical_count = (
        rag_store
        .count_student_observations(
            student_id
        )
    )

    print(
        f"[3/5] Existing historical "
        f"observations for "
        f"{student_id}: "
        f"{historical_count}"
    )

    if historical_count == 0:

        print(
            "[3/5] NOTE: This is the "
            "student's first known "
            "audio history."
        )

    else:

        print(
            "[3/5] Historical evidence "
            "will be available to "
            "semantic search."
        )

    # ========================================================
    # STEP 4 — OLLAMA
    # ========================================================

    reasoner = (
        OllamaReasoner(
            model=OLLAMA_MODEL,
            base_url=OLLAMA_BASE_URL,
            timeout=OLLAMA_TIMEOUT,
            max_retries=(
                OLLAMA_MAX_RETRIES
            ),
        )
    )

    # ========================================================
    # STEP 4 — LANGGRAPH
    # ========================================================

    print()
    print(
        "[4/5] Starting LangGraph "
        "semantic ReAct agent..."
    )

    print()

    print(
        "[Runner] Configuration"
    )

    print(
        f"[Runner] Student ID: "
        f"{student_id}"
    )

    print(
        f"[Runner] Max ReAct steps: "
        f"{MAX_REACT_STEPS}"
    )

    print(
        f"[Runner] Chunk size: "
        f"{CHUNK_SECONDS:.1f}s"
    )

    print(
        f"[Runner] Chunk overlap: "
        f"{OVERLAP_SECONDS:.1f}s"
    )

    print(
        f"[Runner] Semantic top-k: "
        f"{SEMANTIC_TOP_K}"
    )

    print(
        f"[Runner] Ollama model: "
        f"{OLLAMA_MODEL}"
    )

    print(
        f"[Runner] Embedding model: "
        f"{EMBEDDING_MODEL}"
    )

    print(
        "[Runner] Student-scoped "
        "semantic retrieval: ON"
    )

    print(
        "[Runner] Agent decisions "
        "excluded from evidence: ON"
    )

    print(
        "[Runner] Dynamic LangGraph "
        "recursion limit: ON"
    )

    agent = (
        AudioReActGraph(
            rag_store=rag_store,

            reasoner=reasoner,

            low_confidence_threshold=(
                LOW_CONFIDENCE_THRESHOLD
            ),

            high_confidence_threshold=(
                HIGH_CONFIDENCE_THRESHOLD
            ),

            max_react_steps=(
                MAX_REACT_STEPS
            ),

            semantic_top_k=(
                SEMANTIC_TOP_K
            ),
        )
    )

    # ========================================================
    # RUN
    # ========================================================

    try:

        final_state = agent.run(
            audio_file_id=(
                audio_file_id
            ),

            source_file=str(
                audio_path
            ),

            chunks=chunks,

            student_id=student_id,

            precomputed_analyses=(
                precomputed_analyses
            ),
        )

    except Exception as exc:

        print()
        print(
            "[ERROR] LangGraph execution failed:"
        )

        print(
            exc
        )

        raise

    # ========================================================
    # STEP 5 — REPORT
    # ========================================================

    report_path = (
        generate_report(
            final_state=final_state,
            audio_file_id=(
                audio_file_id
            ),
            source_file=str(
                audio_path
            ),
            student_id=student_id,
        )
    )

    print()
    print(
        "[5/5] Report generated"
    )

    # ========================================================
    # SUMMARY
    # ========================================================

    results = final_state.get(
        "report_results",
        [],
    )

    review_count = sum(
        1
        for result in results
        if result.get(
            "review_required",
            False,
        )
    )

    context_count = sum(
        1
        for result in results
        if result.get(
            "context_used",
            False,
        )
    )

    reanalysis_count = sum(
        1
        for result in results
        if result.get(
            "reanalyzed",
            False,
        )
    )

    label_summary = {}

    for result in results:

        label = result.get(
            "assigned_label",
            "OTHER",
        )

        label_summary[label] = (
            label_summary.get(
                label,
                0,
            )
            + 1
        )

    print()
    print(
        "========================================"
    )

    print(
        "FINAL PIPELINE SUMMARY"
    )

    print(
        "========================================"
    )

    print(
        f"Student: "
        f"{student_id}"
    )

    print(
        f"Report: "
        f"{report_path.relative_to(PROJECT_ROOT)}"
    )

    print(
        f"Chunks processed: "
        f"{len(results)}"
    )

    print(
        f"Chunks with semantic context: "
        f"{context_count}"
    )

    print(
        f"Chunks requiring review: "
        f"{review_count}"
    )

    print(
        f"Chunks reanalyzed: "
        f"{reanalysis_count}"
    )

    print()

    print(
        "Label summary:"
    )

    for label, count in sorted(
        label_summary.items()
    ):

        print(
            f"  {label}: {count}"
        )

    print()

    print(
        "Done."
    )


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()