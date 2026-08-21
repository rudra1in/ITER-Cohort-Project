"""
Ingest + analyze a new test set from the command line.
No frontend, no running FastAPI server required.

Usage:
    python ingest_cli.py TEST_002 data/raw/TEST_002
    python ingest_cli.py TEST_002 data/raw/TEST_002 --index   # also build FAISS index
"""

import sys
import argparse

from app.database import Database
from app.detector import YOLODetector
from app.tracker import PersonTracker
from app.pose_analyzer import PoseAnalyzer
from app.event_engine import EventEngine
from app.ingestion import IngestionService
from app.analysis import BehavioralAnalysisService

from app.config import (
    YOLO_MODEL, YOLO_POSE_MODEL,
    TRACK_CONFIDENCE, POSE_CONFIDENCE,
    MIN_EVENT_DURATION, EVENT_GAP_SECONDS
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("test_id")
    parser.add_argument("source_directory")
    parser.add_argument("--index", action="store_true",
                         help="Also build the FAISS/RAG index after analysis")
    args = parser.parse_args()

    db = Database()
    detector = YOLODetector(model_name=YOLO_MODEL)

    print(f"Ingesting {args.test_id} from {args.source_directory} ...")
    ingestion = IngestionService(database=db, detector=detector)
    ingest_result = ingestion.ingest_test(args.test_id, args.source_directory)
    print("Ingest result:", ingest_result)

    print("Running tracking + pose analysis + event detection ...")
    tracker = PersonTracker(model_name=YOLO_MODEL, confidence=TRACK_CONFIDENCE)
    pose_analyzer = PoseAnalyzer(model_name=YOLO_POSE_MODEL, confidence=POSE_CONFIDENCE)
    event_engine = EventEngine(min_duration=MIN_EVENT_DURATION, gap_seconds=EVENT_GAP_SECONDS)

    analysis = BehavioralAnalysisService(
        database=db, tracker=tracker,
        pose_analyzer=pose_analyzer, event_engine=event_engine
    )
    analysis_result = analysis.analyze_test(args.test_id)
    print("Analysis result: frames=%s observations=%s events=%s" % (
        analysis_result["frames_analyzed"],
        analysis_result["observations"],
        analysis_result["events"],
    ))

    if args.index:
        from app.embeddings import EmbeddingService
        from app.vector_store import FAISSVectorStore
        from app.indexer import EventIndexer
        from app.config import EMBEDDING_MODEL, VECTOR_DIR

        print("Building FAISS index ...")
        embedding_service = EmbeddingService(EMBEDDING_MODEL)
        vector_store = FAISSVectorStore(directory=VECTOR_DIR, dimension=384)
        indexer = EventIndexer(database=db, embedding_service=embedding_service,
                                vector_store=vector_store)
        index_result = indexer.index_test(args.test_id)
        print("Index result:", index_result)

    print(f"\nDone. {args.test_id} will now appear in the Streamlit sidebar dropdown.")


if __name__ == "__main__":
    main()
