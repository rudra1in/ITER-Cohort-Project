import uuid
from fastapi import (
    FastAPI,
    HTTPException
)
from pydantic import BaseModel
from app.database import Database
from app.detector import YOLODetector
from app.ingestion import (
    IngestionService
)
from app.tracker import (
    PersonTracker
)
from app.pose_analyzer import (
    PoseAnalyzer
)
from app.event_engine import (
    EventEngine
)
from app.analysis import (
    BehavioralAnalysisService
)
from app.embeddings import (
    EmbeddingService
)
from app.vector_store import (
    FAISSVectorStore
)
from app.indexer import (
    EventIndexer
)
from app.hybrid_search import (
    HybridRetriever
)
from app.memory import (
    ConversationMemory
)
from app.llm import (
    LocalLLM
)
from app.rag import (
    RAGService
)
from app.config import (
    YOLO_MODEL,
    YOLO_POSE_MODEL,
    TRACK_CONFIDENCE,
    POSE_CONFIDENCE,
    MIN_EVENT_DURATION,
    EVENT_GAP_SECONDS,
    EMBEDDING_MODEL,
    VECTOR_DIR,
    LLM_MODEL,
    LLM_PROVIDER,
    OLLAMA_MODEL,
    OLLAMA_BASE_URL,
    MEMORY_LIMIT,
    GEMINI_API_KEY,
    GEMINI_MODEL,
    GEMINI_CONFIDENCE_THRESHOLD,
    FACE_LANDMARKER_MODEL_PATH
)
from app.agents.investigation import (
    InvestigationCrew
)
from app.langgraph_orchestrator import (
    LangGraphOrchestrator
)
from app.face_refiner import (
    FaceMeshRefiner
)
from app.gemini_fallback import (
    GeminiEscalation
)

 
# APP
 

app = FastAPI(
    title="Offline Behavioral Analysis RAG",
    version="0.6"
)

 
# DATABASE
 
database = Database()


# PART 1 INGESTION
 

detector = YOLODetector(
    model_name=YOLO_MODEL
)
ingestion = IngestionService(
    database=database,
    detector=detector
)
 
# PART 2  ANALYSIS
 

tracker = PersonTracker(
    model_name=YOLO_MODEL,
    confidence=TRACK_CONFIDENCE
)
face_refiner = FaceMeshRefiner(
    model_path=FACE_LANDMARKER_MODEL_PATH
)

pose_analyzer = PoseAnalyzer(
    model_name=YOLO_POSE_MODEL,
    confidence=POSE_CONFIDENCE,
    face_refiner=face_refiner
)

event_engine = EventEngine(
    min_duration=MIN_EVENT_DURATION,
    gap_seconds=EVENT_GAP_SECONDS
)

gemini_escalation = GeminiEscalation(
    api_key=GEMINI_API_KEY,
    model=GEMINI_MODEL,
    confidence_threshold=GEMINI_CONFIDENCE_THRESHOLD
)

behavior_analysis = (
    BehavioralAnalysisService(
        database=database,
        tracker=tracker,
        pose_analyzer=pose_analyzer,
        event_engine=event_engine,
        gemini_escalation=gemini_escalation
    )
)
 
# PART 3  EMBEDDINGS & VECTOR STORE
 

embedding_service = EmbeddingService(
    EMBEDDING_MODEL
)

#as all-MiniLM-L6-v2 produces 384d vectors.
embedding_dimension = 384

vector_store = FAISSVectorStore(
    directory=VECTOR_DIR,
    dimension=embedding_dimension
)
 
# INDEXER
 

event_indexer = EventIndexer(
    database=database,
    embedding_service=embedding_service,
    vector_store=vector_store
)
 
# RETRIEVER
 

retriever = HybridRetriever(
    database=database,
    embedding_service=embedding_service,
    vector_store=vector_store
)
 
# MEMORY
 

memory = ConversationMemory(
    database=database,
    limit=MEMORY_LIMIT
)

# LOCAL LLM
 

llm = LocalLLM(
    gemini_model=LLM_MODEL,
    gemini_api_key=GEMINI_API_KEY,
    ollama_model=OLLAMA_MODEL,
    ollama_base_url=OLLAMA_BASE_URL,
    temperature=0,
    default_provider=LLM_PROVIDER
)
 
# RAG
 

rag = RAGService(
    database=database,
    retriever=retriever,
    memory=memory,
    llm=llm
)

# CREWAI INVESTIGATION CREW
 

investigation_crew = InvestigationCrew(
    database=database,
    retriever=retriever,
    llm_router=llm
)

# LANGGRAPH ORCHESTRATOR
 

orchestrator = LangGraphOrchestrator(
    rag=rag,
    investigation_crew=investigation_crew,
    database=database,
    retriever=retriever,
    embedding_service=embedding_service,
    memory=memory
)


 
# REQUEST MODELS
 

class IngestRequest(
    BaseModel
):

    test_id: str

    directory: str


class ChatRequest(
    BaseModel
):

    test_id: str

    session_id: str | None = None

    question: str


class SwitchProviderRequest(
    BaseModel
):

    provider: str


 
# ROOT
 

@app.get("/")
def root():

    return {

        "project":
            "Offline Behavioral Analysis RAG",

        "version":
            "0.6.0",

        "orchestrator":
            "LangGraph ReAct",

        "status":
            "running"
    }


 
# HEALTH
 

@app.get(
    "/health"
)
def health():

    # LLM check depends on which provider is currently active.Ollama is local, so a quick reachability ping is
    # cheap and worth doing directly.
    if llm.provider == "ollama":

        llm_ok = False
        try:
            import requests as _req
            resp = _req.get(
                f"{OLLAMA_BASE_URL}/api/tags",
                timeout=3
            )
            llm_ok = resp.status_code == 200
        except Exception:
            pass

    else:

        llm_ok = llm.gemini_configured

    return {

        "api":
            "ok",

        "vector_store_count":
            vector_store.count(),

        "llm_provider":
            llm.provider,

        "llm_model":
            LLM_MODEL if llm.provider == "gemini" else OLLAMA_MODEL,

        "llm_reachable":
            llm_ok,

        "orchestrator":
            "langgraph"
    }


 
# LLM PROVIDER (status + runtime switch)
 

@app.get(
    "/llm/status"
)
def llm_status():

    return llm.status()


@app.post(
    "/llm/switch"
)
def llm_switch(
    request: SwitchProviderRequest
):

    try:

        llm.switch(
            request.provider
        )

        return llm.status()

    except (ValueError, RuntimeError) as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


 
# TESTS LIST
 

@app.get(
    "/tests"
)
def get_tests():

    return {
        "tests":
            database.get_tests()
    }


 
# INGEST
 

@app.post(
    "/tests/ingest"
)
def ingest_test(
    request: IngestRequest
):

    try:

        return ingestion.ingest_test(
            test_id=request.test_id,
            source_directory=request.directory
        )

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


 
# ANALYZE
 

@app.post(
    "/tests/{test_id}/analyze"
)
def analyze_test(
    test_id: str
):

    try:

        return behavior_analysis.analyze_test(
            test_id
        )

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


 
# INDEX
 

@app.post(
    "/tests/{test_id}/index"
)
def index_test(
    test_id: str
):

    try:

        return event_indexer.index_test(
            test_id
        )

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


 
# CLUSTER
 

@app.post(
    "/tests/{test_id}/cluster"
)
def cluster_test(
    test_id: str,
    algorithm: str = "dbscan"
):

    try:

        from app.clustering import EventClusterer

        clusterer = EventClusterer(
            algorithm=algorithm
        )

        events = database.get_events(
            test_id
        )

        results = clusterer.cluster(
            events
        )

        for result in results:

            database.update_event_cluster(
                result["event_id"],
                result["cluster_id"],
                result["cluster_label"],
                result["is_suspicious"]
            )

        suspicious_count = sum(
            1
            for result in results
            if result["is_suspicious"]
        )

        return {
            "test_id": test_id,
            "algorithm": algorithm,
            "events_clustered": len(results),
            "suspicious": suspicious_count,
            "common": len(results) - suspicious_count
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


 
# CHAT
 

@app.post(
    "/chat"
)
def chat(
    request: ChatRequest
):

    try:

        session_id = (
            request.session_id
            or
            f"SESSION_"
            f"{uuid.uuid4().hex[:10]}"
        )

        memory.create_session(
            session_id,
            request.test_id
        )

        result = orchestrator.run(

            test_id=request.test_id,

            session_id=session_id,

            question=request.question
        )

        result[
            "session_id"
        ] = session_id

        return result

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


 
# EVENTS
 

@app.get(
    "/tests/{test_id}/events"
)
def events(
    test_id: str,
    suspicious_only: bool = False
):

    return {

        "test_id":
            test_id,

        "events":
            database.get_events(
                test_id,
                suspicious_only=suspicious_only
            )
    }


 
# SUMMARY
 

@app.get(
    "/tests/{test_id}"
)
def summary(
    test_id: str
):

    return database.get_test_summary(
        test_id
    )


 
# CANDIDATES
 

@app.get(
    "/tests/{test_id}/candidates"
)
def get_candidates(
    test_id: str
):

    return {
        "test_id": test_id,
        "candidates": database.get_candidates(test_id)
    }


 
# CANDIDATE TIMELINE
 

@app.get(
    "/tests/{test_id}/candidates/{candidate_id}/timeline"
)
def candidate_timeline(
    test_id: str,
    candidate_id: str
):

    return {
        "test_id": test_id,
        "candidate_id": candidate_id,
        "events": database.get_candidate_timeline(
            test_id,
            candidate_id
        )
    }


 
# STATISTICS
 

@app.get(
    "/tests/{test_id}/statistics"
)
def test_statistics(
    test_id: str
):

    return {
        "test_id": test_id,
        "statistics": database.get_test_statistics(test_id)
    }