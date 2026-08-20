# Offline Behavioral Analysis & Evidence RAG System

An enterprise-grade, modular, offline-first post-exam behavioral forensics and retrieval system.

This system processes sequences of candidate image frames captured during online or offline examinations after the test completes. It filters redundant frames, tracks candidate identities, extracts spatial pose/orientation features, converts observations into descriptive behavioral events, groups common behaviors via density-based clustering, indices findings into a dual-search hybrid retrieval engine, and exposes a conversational Q&A interface powered by a **LangGraph ReAct state machine** and **CrewAI multi-agent crews**.

> [!IMPORTANT]
> **Evidence, Not Conclusions — Safety Guardrails:**
> This system is designed as an evidence-review tool for human verification, **not** an automated cheating detector. All generated text, prompts, and agent workflows are strictly bound by non-accusatory rules. The system will describe objective observations (e.g., *"mobile phone visible for 12 seconds"*, *"head oriented left repeatedly"*) but will **never** declare that a candidate definitely cheated.

---

## 📖 Table of Contents
1. [Key Features & Capabilities](#-key-features--capabilities)
2. [Technology Stack](#-technology-stack)
3. [System Architecture & Workflow](#-system-architecture--workflow)
4. [Agentic Orchestration](#-agentic-orchestration)
   - [LangGraph ReAct Orchestrator](#langgraph-react-orchestrator)
   - [CrewAI Investigation Crew](#crewai-investigation-crew)
5. [Behavioral Event Engine & Clustering](#-behavioral-event-engine--clustering)
6. [Directory Structure](#-directory-structure)
7. [Installation & Setup](#-installation--setup)
8. [Configuration & Environment Variables](#-configuration--environment-variables)
9. [Running the Application](#-running-the-application)
10. [API Reference Documentation](#-api-reference-documentation)

---

## 🌟 Key Features & Capabilities
*   **Offline-First CV Pipeline, Cloud LLM**: The computer-vision and retrieval pipeline (YOLOv11, Sentence-Transformers, FAISS) runs entirely on your local machine; conversational reasoning is powered by the Google Gemini API.
*   **Intelligent Data Ingestion & Filtering**: Suppresses duplicate/near-duplicate frames using pixel Mean Squared Error (MSE) and perceptual hashing (`pHash`) to minimize downstream model computation and database bloat.
*   **Robust Spatial Tracking & Pose Estimation**: Tracks candidates across frame sequences using ByteTrack, estimates yaw and pitch with YOLOv11-Pose, and refines gaze orientation using MediaPipe Face Mesh.
*   **Dual-Index Hybrid Retrieval**: Combines semantic vector similarity (FAISS) with lexical keyword matching (SQLite FTS5 BM25) using Reciprocal Rank Fusion (RRF).
*   **Advanced Conversation Graph**: Handles complex, multi-hop queries using a stateful LangGraph orchestrator with in-memory checkpointing.
*   **Interactive Review Dashboard**: An elegant 4-tab Streamlit dashboard providing a conversational Q&A tab, filterable event viewer, candidate timeline grids, and pipeline control boards.

---

## 🛠 Technology Stack

### Computer Vision & Processing
*   **Ultralytics YOLOv11** (`yolo11n.pt` & `yolo11n-pose.pt`): Bounding boxes for people, phones, papers, and 17 skeletal keypoint extraction.
*   **ByteTrack**: Spatial Kalman filtering to persist identity across frames.
*   **MediaPipe Face Mesh**: 3D perspective-n-point face modeling for sub-degree head direction yaw/pitch calculations.
*   **OpenCV & Pillow**: Structural validation, pixel manipulation, and temporal change tracking.
*   **ImageHash**: Perceptual hashing (`pHash`) utilizing DCT coefficient comparison.

### Vector Embedding, Storage & Search
*   **SQLite3**: Structured storage of frames, detections, observations, events, and conversation memory.
*   **SQLite FTS5**: Virtual tables indexing lexical metadata using the BM25 text-relevance algorithm.
*   **FAISS (`faiss-cpu`)**: Dense vector storage using Flat L2/Inner Product search indices.
*   **Sentence-Transformers** (`all-MiniLM-L6-v2`): Encodes event descriptions into 384-dimensional dense vectors.
*   **Reciprocal Rank Fusion (RRF)**: Merges sparse keyword ranks and dense vector similarity ranks ($65\%$ Vector weight, $35\%$ Keyword weight).

### Machine Learning, Agents & Orchestration
*   **LangGraph**: Stateful, cyclic graph engine running the core query executor.
*   **CrewAI**: Orchestrates multi-agent teams using sequential process pipelines.
*   **LangChain Expression Language (LCEL)**: RAG prompts and parse pipes constructed with `ChatPromptTemplate`, `StrOutputParser`, and `JsonOutputParser`.
*   **Google Gemini API + Ollama**: Dual, runtime-switchable LLM backends for RAG and CrewAI (default Gemini `gemini-3.6-flash`, switchable to local Ollama `llama3.2:1b` from the Streamlit sidebar with no restart), plus Gemini as the failsafe text reasoning model for resolving locally ambiguous frames.

---

## 🏗 System Architecture & Workflow

The system operates via a sequential ingestion-to-retrieval pipeline:

```
JPEG Frames (Raw Photos)
    │
    ▼
[Data Ingestion] ──► Validation ──► SHA-256 (Exact Dupes) ──► pHash (Near Dupes) ──► Change (MSE)
    │
    ▼
[Computer Vision] ──► YOLOv11 (BBoxes) ──► ByteTrack (IDs) ──► YOLOv11-Pose (Keypoints) ──► MediaPipe (Face Mesh)
    │
    ▼
[Event Engine] ──► 6 Behavioral Event Types ──► Feature Engineering
    │
    ▼
[Clustering] ──► Normalization (StandardScaler) ──► DBSCAN / HDBSCAN ──► Flag Outliers (Suspicious)
    │
    ▼
[Storage & Indexing]
    ├── SQLite Tables ──► FTS5 Virtual Table (Lexical Keyword BM25)
    └── Sentence-Transformers (all-MiniLM-L6-v2) ──► FAISS Vector Store (Semantic)
    │
    ▼
[Orchestrator] ──► LangGraph Graph Loop (Planning ──► Hybrid Retrieval ──► Sufficiency Gate)
                      ├── Sufficient  ──► Generate Answer (Strict non-accusatory guidelines)
                      ├── Needs Tools ──► ReAct Tool Loop (Timeline, Compare, Search, etc.)
                      └── Needs Crew  ──► CrewAI Investigation Crew (4-Agent Pipeline)
```

---

## 🤖 Agentic Orchestration

### LangGraph ReAct Orchestrator
The conversational system is managed by a stateful graph ([`app/langgraph_orchestrator.py`](file:///d:/devs/24E3/app/langgraph_orchestrator.py)) compiling 7 distinct nodes:
*   `plan_query`: Employs LCEL to parse the user's intent, resolving pronouns and target candidate names.
*   `retrieve`: Searches FAISS and SQLite FTS5 using Reciprocal Rank Fusion.
*   `assess_sufficiency`: Directs flow to RAG, the ReAct loop, or a CrewAI investigation depending on prompt complexity.
*   `use_tools`: Cyclic ReAct loop matching tools to missing details (runs up to 3 times).
*   `route_to_crew`: Handoff node spawning the CrewAI team for deep/comparative queries.
*   `generate_answer`: Final synthesis node returning safety-filtered descriptions.
*   `save_memory`: Persists transaction history to SQLite conversation logs.

### CrewAI Investigation Crew
For queries requiring comprehensive evaluation (e.g., *"summarize RAM's anomalies and compare them to the average"*), the orchestrator executes a sequential multi-agent crew:

```
Retrieval Analyst ──► Evidence Analyst ──► Review Analyst ──► Report Summary Agent
```

1.  **Behavioral Retrieval Analyst**:
    *   *Role*: Searcher & Collector.
    *   *Goal*: Interface with database queries and semantic hybrid indexes to retrieve relevant observations.
    *   *Tools*: `search_behavioral_events`, `get_candidate_events`, `get_suspicious_events`, `compare_candidates`.
2.  **Evidence Analyst**:
    *   *Role*: Forensic Parser.
    *   *Goal*: Normalizes event linkages, timestamps, durations, confidence scores, and physical frame IDs without inventing facts.
3.  **Behavioral Review Analyst**:
    *   *Role*: Compliance Gatekeeper.
    *   *Goal*: Evaluates findings under strict non-accusatory guidelines. Separates objective observation from inference and filters forbidden words (e.g., "cheating").
4.  **Investigation Report Writer**:
    *   *Role*: Editor.
    *   *Goal*: Compiles the parsed outputs into a clean markdown document divided into clear sections: Overview, Behavioral Observations, Flagged Outliers, and the System Disclaimer.

---

## 🔍 Behavioral Event Engine & Clustering

### The 6 Behavioral Event Types
*   `repeated_side_looking`: Gaze deviations left or right exceeding a $\pm 15^\circ$ yaw angle.
*   `phone_visible`: Object classifier locating cell phone bounding boxes.
*   `body_turned_away`: Structural pose analysis identifying body direction facing side-profile or away.
*   `excessive_movement`: Spatial movement score surpassing the running average displacement limit.
*   `absent_from_frame`: Camera tracking returns 0 detected candidate frames.
*   `extra_person_detected`: Multiple people identified in candidate's workspace area.

### Density-Based Clustering
To filter out noise caused by standard rooms or test structures (e.g., looking down at a keyboard or facing a window), the system clusters events using DBSCAN or HDBSCAN.
*   **Features mapped**: `[One-Hot Event Type, Duration, Avg Pose Confidence, Evidence Frame Count]`.
*   **Common Events**: Dense clusters (e.g. routine looking down) represent baseline room anomalies.
*   **Suspicious Events**: Noise points (Cluster ID = `-1`) and micro-clusters representing unique outlier deviations.

---

## 📂 Directory Structure

```
.
├── app/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── investigation.py          # CrewAI agents and tasks declaration
│   │   └── tools.py                  # Dual-purpose LangChain + CrewAI tools
│   ├── __init__.py
│   ├── analysis.py                   # Behavioral pipeline service
│   ├── behavior.py                   # Visual feature vector extraction
│   ├── clustering.py                 # DBSCAN/HDBSCAN clustering engine
│   ├── config.py                     # Environment variables & paths config
│   ├── database.py                   # SQLite tables, indexes, FTS5 & queries
│   ├── detector.py                   # YOLOv11 bounding box inference
│   ├── embeddings.py                 # Sentence-transformers wrapper
│   ├── event_engine.py               # 6 behavioral event state machines
│   ├── face_refiner.py               # MediaPipe Face Mesh gaze resolver
│   ├── gemini_fallback.py            # Ambiguity escalation failsafe module
│   ├── hybrid_search.py              # FTS5 BM25 + FAISS RRF search engine
│   ├── image_utils.py                # Image validation, pHash, SHA256 & MSE
│   ├── indexer.py                    # Vector store update scheduler
│   ├── ingestion.py                  # De-duplication and validation pipe
│   ├── langgraph_orchestrator.py     # Stateful ReAct conversation graph
│   ├── llm.py                        # Local LLM connector wrapper
│   ├── main.py                       # FastAPI application router endpoints
│   ├── memory.py                     # Conversation history parser
│   ├── orchestrator.py               # Orchestrator compatibility shim
│   ├── pose_analyzer.py              # YOLO-Pose keypoints mapping
│   ├── tracker.py                    # ByteTrack coordinates tracking
│   └── vector_store.py               # FAISS vector store management
├── data/                             # Created automatically on launch
│   ├── raw/                          # Directory for unprocessed test folders
│   ├── processed/                    # Normalized target images output
│   ├── reports/                      # Exchanged report storage
│   └── vector_store/                 # FAISS binaries and metadata JSONs
├── ingest_cli.py                     # CLI scripting ingestion utility
├── repair_data.py                    # Path normalization DB repair script
├── req.txt                           # Project python requirements
├── streamlit.py                      # Main 4-tab reviewer dashboard
└── yolo11n-pose.pt / yolo11n.pt      # Precompiled weight assets
```

---

## ⚙️ Configuration & Environment Variables

Create a `.env` file in the root directory to customize parameters:

```env
# Database & Folder Paths
DATA_DIR="data"
DATABASE_PATH="data/app.db"
VECTOR_DIR="data/vector_store"

# Vision Thresholds
TRACK_CONFIDENCE="0.35"
POSE_CONFIDENCE="0.35"
PHASH_THRESHOLD="8"
CHANGE_THRESHOLD="0.08"

# Event Engine Gates
LOOK_LEFT_THRESHOLD="-15"
LOOK_RIGHT_THRESHOLD="15"
MIN_EVENT_DURATION="3"
EVENT_GAP_SECONDS="3"

# Embedding & LLM Configurations
EMBEDDING_MODEL="sentence-transformers/all-MiniLM-L6-v2"

# Dual LLM provider - switchable at runtime, see "LLM Provider Toggle" below
LLM_PROVIDER="gemini"                  # which one is active on startup
LLM_MODEL="gemini-3.6-flash"
GEMINI_API_KEY="your-gemini-api-key"
OLLAMA_MODEL="llama3.2:1b"
OLLAMA_BASE_URL="http://localhost:11434"

# Optional: separate model/threshold for vision escalation on
# ambiguous frames (can reuse the same key as above)
GEMINI_MODEL="gemini-3.6-flash"
GEMINI_CONFIDENCE_THRESHOLD="0.4"
```

---

## 🔀 LLM Provider Toggle

The main conversational LLM (used by RAG, LangGraph, and CrewAI) can be
switched between the Gemini API and a local Ollama model **at
runtime, with no restart**:

*   **Streamlit UI**: a radio toggle in the sidebar under "LLM
    Provider". Switching it calls the API immediately and reruns the
    page - your next question uses the new provider.
*   **API**: `GET /llm/status` to see the current provider and
    whether each backend is configured; `POST /llm/switch` with
    `{"provider": "gemini"}` or `{"provider": "ollama"}` to switch.

Switching to Ollama requires `ollama serve` to be running locally with
the configured model pulled (`ollama pull llama3.2:1b`). Switching to
Gemini requires `GEMINI_API_KEY` to be set - attempting to switch to
Gemini without a key returns a clear 400 error rather than silently
failing later.

Under the hood: RAGService's LangChain chains, the LangGraph
orchestrator's direct LLM calls, and CrewAI's agents all read the
active provider dynamically (see `app/llm.py`) - none of them need to
be rebuilt when you switch, so a conversation can continue seamlessly
across a provider change.

---

## 🚀 Running the Application

### Step 1: Initialize raw photos
Place candidate photo directory structures under `data/raw/{TEST_ID}/{CANDIDATE_NAME}/`, containing a timestamp in each filename matching patterns like `HH_MM_SS`, `HH:MM:SS`, or `HHMMSS`.
```
data/raw/TEST_001/RAM/frame_10_20_05.jpg
data/raw/TEST_001/RAM/frame_10_20_08.jpg
```

### Step 2: Command line ingestion (Alternate)
You can trigger ingestion, tracking, indexing, and clustering through the CLI script:
```bash
# Ingest, analyze and build the vector index
python ingest_cli.py TEST_001 data/raw/TEST_001 --index
```

### Step 3: Run the FastAPI backend
```bash
uvicorn app.main:app --reload
```

### Step 4: Run the Review Dashboard
Open a secondary terminal and start the Streamlit application:
```bash
streamlit run streamlit.py
```
