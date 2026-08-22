# AI DSA Coach (CodeMentor)

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-4169E1.svg?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![pgvector](https://img.shields.io/badge/pgvector-0.5+-336791.svg?style=flat)](https://github.com/pgvector/pgvector)
[![Google Gemini](https://img.shields.io/badge/Google_Gemini-API-4285F4.svg?style=flat&logo=google&logoColor=white)](https://ai.google.dev/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Agent_Orchestration-1C1C1C.svg?style=flat)](https://github.com/langchain-ai/langgraph)

An intelligent, production-ready Data Structures and Algorithms (DSA) mentoring system powered by **FastAPI**, **Streamlit**, **LangGraph agent orchestration**, **PostgreSQL with pgvector hybrid retrieval**, and **Google Gemini LLM**. 

Unlike conventional competitive programming platforms that provide pass/fail verdicts or dump full code solutions, AI DSA Coach acts as an interactive Socratic tutor. It analyzes student Python code via AST parsing, runs isolated test-case subprocess execution, retrieves domain-specific DSA knowledge through hybrid vector-keyword search and cross-encoder reranking, and generates progressive, structured coaching hints tailored to individual learning history.

---

## 1. Project Highlights

- **Interactive DSA Workspace**: Dual-panel Streamlit UI with problem specifications, constraints, code editor, test case output console, and AI coaching panels.
- **AST Static Code Analysis**: Real-time Python Abstract Syntax Tree (`ast`) linting detecting syntax errors before code execution.
- **Isolated Code Execution**: Secure subprocess execution with configurable timeout handling (default 3s), output truncation (max 10,000 chars), and detailed per-test-case validation.
- **LangGraph Agent Orchestration**: Stateful graph execution that dynamically routes requests across specialized nodes based on syntax errors, runtime failures, wrong answers, timeouts, or accepted solutions.
- **Hybrid Search RAG Pipeline**: Combines dense vector search (768-dim Gemini embeddings via `pgvector` HNSW index) and full-text keyword search (`tsvector` GIN index) fused via Reciprocal Rank Fusion (RRF, $K=60$).
- **Cross-Encoder Reranking**: Re-scores candidate knowledge chunks using `BAAI/bge-reranker-v2-m3` combined with domain-specific metadata relevance scoring.
- **Gemini-Powered Socratic Coaching**: Structured JSON output forcing the LLM to provide targeted diagnoses, progressive hints (Levels 1–5), pattern identification, and complexity analysis without spoiling full code solutions.
- **Student History & Memory Tracking**: PostgreSQL-backed persistent attempt tracking (`student_attempts`) analyzing past errors and recurring mistakes across attempts.
- **Observability & Token Tracking**: PostgreSQL-backed token usage logging (`token_usage`) capturing prompt tokens, completion tokens, model latency, and retrieved chunk counts per interaction.

---

## 2. System Architecture


![AI DSA Coach System Architecture](architecture.png)



### Component Summary

1. **Streamlit Frontend (`app.py`, `frontend/`)**: Manages the dual-panel web interface, state management, interactive code editing, API client communication, and animated feedback rendering.
2. **FastAPI Backend (`backend/app.py`, `backend/routes/`)**: Exposes REST endpoints (`/api/coach`, `/api/code/execute`, `/api/code/analyze`, `/api/rag/search`, `/api/problems`), handles CORS, initializes database schemas, and invokes the LangGraph agent.
3. **LangGraph Agent (`backend/agent/`)**: Coordinates problem loading, memory retrieval, AST syntax verification, test-case code execution, conditional routing, RAG query construction, reranking, model selection, and prompt assembly into a unified state graph.
4. **Code Execution Engine (`backend/services/code_executor.py`)**: Executes student code safely in temporary subprocess containers with strict timeout limits and per-test-case validation.
5. **RAG & Retrieval Engine (`backend/retrieval/`, `backend/rag/`)**: Performs metadata-aware hybrid vector-keyword retrieval on PostgreSQL/pgvector and re-ranks results with a cross-encoder transformer model.
6. **AI Coach Service (`backend/services/ai_coach.py`)**: Interacts with the Google Gemini API using Pydantic structured response schemas (`CoachAIResponse`) and system instructions enforcing Socratic coaching rules.
7. **PostgreSQL Data Layer (`backend/database.py`, `backend/sql/schema.sql`)**: Relational database leveraging `pgvector` for 768-dimensional vector cosine distance search and GIN indexes for full-text keyword search.

---

## 3. End-to-End Request Flow

![Sequence Diagram](workflow.png)

### Retrieval Mechanics

- **Chunking Strategy**: Rather than arbitrary character-count sliding windows, document chunking is **semantic and section-based** (`chunker.py`). Documents are segmented by `problem`, `intuition`, `approach`, `algorithm`, `example`, `mistakes`, `complexity`, and `solution`.
- **Embeddings**: Generated using Google Gemini Embeddings (`models/gemini-embedding-001` or `text-embedding-004`) constrained to **768 dimensions**.
- **Vector Search (`pgvector`)**: Performs cosine distance similarity matching (`<=>` operator) against 768-dimensional vectors stored in `dsa_chunks`, accelerated by an HNSW index (`vector_cosine_ops`).
- **Keyword Search (`tsvector`)**: Performs PostgreSQL full-text search matching query terms against pre-computed `tsvector` columns indexed with a GIN index.
- **Hybrid Fusion (RRF)**: Reciprocal Rank Fusion combines vector and keyword rankings without requiring score normalization:
  $$\text{RRF\_Score}(d) = \sum_{m \in M} \frac{1}{K + r_m(d)}$$
  where $K = 60$, and $r_m(d)$ is the rank of document $d$ in retrieval method $m$.
- **Cross-Encoder Reranking**: The candidate pool (top 15–20 candidates) is re-evaluated using `sentence-transformers` with `BAAI/bge-reranker-v2-m3`, paired with a minor metadata relevance bonus for exact topic, pattern, or chunk type alignment.
- **Context Injection**: The top $K$ re-ranked chunks are formatted into a markdown context block injected directly into the Gemini LLM prompt.

---

## 5. Knowledge Base & Dataset

The knowledge base is stored under `data/` as structured JSON files organized into 6 core categories:

| Category | Path | Description | Key Fields |
|---|---|---|---|
| **Concepts** | `data/concepts/` | Core DSA data structures and foundational theory | `title`, `topic`, `subtopic`, `description`, `properties`, `time_complexity`, `space_complexity` |
| **Patterns** | `data/patterns/` | Algorithmic problem-solving paradigms | `title`, `pattern`, `topic`, `when_to_use`, `key_identifiers`, `template_code` |
| **Problems** | `data/problems/` | Problem definitions and constraints | `id`, `title`, `topic`, `subtopic`, `pattern`, `difficulty`, `description`, `constraints`, `examples` |
| **Solutions** | `data/solutions/` | Optimal reference implementations and walkthroughs | `id`, `problem_id`, `language`, `code`, `intuition`, `approach`, `algorithm`, `time_complexity` |
| **Mistakes** | `data/mistakes/` | Catalog of common student misconceptions and bugs | `title`, `topic`, `pattern`, `bad_example`, `corrected_example`, `explanation` |
| **Examples** | `data/examples/` | Worked trace examples and edge-case dry runs | `title`, `topic`, `pattern`, `input_trace`, `execution_walkthrough` |

### Chunk Metadata Attributes

Every chunk stored in the database retains rich metadata for filtered retrieval:

```json
{
  "document_id": "UUID",
  "chunk_type": "problem | intuition | approach | algorithm | example | mistakes | complexity | solution",
  "title": "Document section title",
  "topic": "Arrays | Strings | Linked Lists | Trees | Graphs | Dynamic Programming | etc.",
  "subtopic": "Two Sum | Binary Search | Sliding Window | etc.",
  "pattern": "Two Pointers | Hash Map | Fast & Slow Pointers | etc.",
  "difficulty": "Easy | Medium | Hard",
  "language": "python",
  "time_complexity": "O(N)",
  "space_complexity": "O(N)",
  "source_reference": "data/problems/two_sum.json"
}
```

---

## 6. Agent Architecture (LangGraph)

The agentic workflow is built on **LangGraph** (`StateGraph`) using a centralized state dictionary (`DSAAgentState`).

![LangGraph Workflow](agent.png)

### Node Descriptions

1. **`load_problem_node`**: Fetches the problem specification and test cases from the registry.
2. **`memory_node`**: Fetches past submission records and recurring error patterns for the student from PostgreSQL.
3. **`analyze_code_node`**: Runs static Python AST validation. If syntax errors exist, populates standard error state and bypasses execution.
4. **`execute_code_node`**: Executes Python code against problem test cases in an isolated subprocess with timeout enforcement.
5. **`build_retrieval_query_node`**: Constructs a specialized DSA search query combining problem context, student code, and error trace.
6. **`retrieve_node`**: Executes hybrid vector-keyword retrieval against `dsa_chunks`.
7. **`rerank_node`**: Re-scores candidates via Cross-Encoder and formats Top-$K$ context for the prompt.
8. **`model_router_node`**: Selects the appropriate Gemini model route (`fast`, `debug`, or `coach`).
9. **`coach_node`**: Calls the Gemini API with structured output instructions to produce the final `CoachAIResponse`.
10. **`success_node`**: Invoked when code passes all test cases; calls Gemini to generate time/space complexity feedback and pattern acknowledgement.

---

## 7. AI Model Architecture

The project configures models dynamically through environment variables in `backend/config.py` and `.env`:

| Component | Logical Route | Environment Variable | Default Model | Purpose |
|---|---|---|---|---|
| **Embedding Model** | `embedding` | `GEMINI_EMBEDDING_MODEL` | `models/gemini-embedding-001` | Generates 768-dimensional dense vector embeddings for RAG chunks and search queries |
| **Fast Model** | `fast` | `GEMINI_FAST_MODEL` | `gemini-2.5-flash` | Lightweight model route for syntax error explanations and direct level 1 hints |
| **Debugger Model** | `debug` | `GEMINI_DEBUGGER_MODEL` | `gemini-2.5-flash` | Fast debugging route for runtime exceptions and failed assertion analysis |
| **Coach Model** | `coach` | `GEMINI_COACH_MODEL` | `gemini-2.5-flash` | Primary reasoning model for deep Socratic DSA coaching and complexity analysis |
| **Reranker Model** | `reranker` | `RERANKER_MODEL` | `BAAI/bge-reranker-v2-m3` | Local Cross-Encoder model re-ranking candidate retrieval chunks |

---

## 8. Code Analysis and Execution

![Code Analysis and Execution](codenalayis.png)

### Execution Details
- **Syntax Check (`services/code_analyzer.py`)**: Uses Python's standard `ast.parse()`. Traps `SyntaxError` to capture exact line number, column offset, and message.
- **Subprocess Runner (`services/code_executor.py`)**: Writes code to a temporary file and runs `subprocess.run()` with standard output/error redirection.
- **Test Wrapper**: Wraps student code with a harness that executes `solution(*input)` against expected JSON outputs.
- **Timeout Protection**: Enforces a `CODE_EXECUTION_TIMEOUT` (default 3 seconds). If expired, terminates process and returns `status: timeout`.
- **Output Safety**: Truncates `stdout` and `stderr` to `MAX_OUTPUT_LENGTH` (10,000 chars) to prevent memory exhaustion.

---

## 9. AI Coaching & Progressive Hinting

The coach system operates on a Socratic principle: **never give away the complete code solution immediately**. Instead, feedback is structured via the Pydantic schema `CoachAIResponse`:

```json
{
  "status": "Incorrect",
  "diagnosis": "The code encounters an IndexError on line 5 when accessing nums[i + 1].",
  "explanation": "When i reaches len(nums) - 1, accessing i + 1 reads beyond the bounds of the list.",
  "hint": "Consider adjusting your loop boundary or adding a condition before accessing index i + 1.",
  "concept": "Array Boundary Conditions",
  "pattern": "Two Pointers",
  "complexity_feedback": "Current approach is O(N^2) due to nested loops.",
  "next_action": "Fix loop bounds to prevent out-of-range indexing.",
  "error_line": 5,
  "error_type": "IndexError",
  "hint_level": 1,
  "should_show_solution": false,
  "confidence": 0.95,
  "sources": []
}
```

### Progressive Hint Levels

- **Level 1 (Guiding Question)**: High-level prompt focusing on edge cases or logical assumptions.
- **Level 2 (Concept Direction)**: Points out the relevant data structure property or algorithmic pattern.
- **Level 3 (Problematic Logic)**: Highlights the specific loop, conditional, or variable causing the failure.
- **Level 4 (Correction Guidance)**: Outlines step-by-step structural changes needed to resolve the bug.
- **Level 5 (Full Solution Guidance)**: Detailed pseudocode or explicit structural walkthrough (solution code provided only if explicitly permitted).

---

## 10. Student Memory & Observability

### Persistent History (`student_attempts`)
Each attempt stores:
- `user_id`, `problem_id`, `code`, `language`
- `status` (`accepted`, `syntax_error`, `runtime_error`, `failed`, `timeout`)
- `error_type` (e.g. `SyntaxError`, `ZeroDivisionError`, `AssertionError`)
- `error_line`, `error_message`, `attempts` count, `solved` boolean
- Raw JSON payloads of `execution_result` and `coach_response`

### Telemetry Tracking (`token_usage`)
Every LLM call logs:
- `model_name` and `request_type` (`debug`, `hint`, `coach`)
- `input_tokens`, `output_tokens`, `total_tokens`
- `retrieved_chunks` count
- `latency_ms` execution duration

---

## 11. Database Architecture (ER Diagram)

---

## 12. API Documentation

### Endpoint Summary

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Root health check and service info |
| `GET` | `/health` | Health probe returning `{"status": "healthy"}` |
| `GET` | `/api/problems` | List all available DSA problems |
| `GET` | `/api/problems/{id}` | Retrieve specific DSA problem specification |
| `POST` | `/api/code/analyze` | Perform static Python AST syntax analysis |
| `POST` | `/api/code/execute` | Execute Python code against test cases in subprocess |
| `POST` | `/api/rag/search` | Direct search interface for RAG vector/keyword retrieval |
| `POST` | `/api/coach` | **Main AI Coach Endpoint**: Triggers full LangGraph execution |

### Main Endpoint Request/Response Example

#### `POST /api/coach`

**Request Payload**:
```json
{
  "user_id": "student_123",
  "problem_id": "two-sum",
  "code": "def solution(nums, target):\n    for i in range(len(nums)):\n        for j in range(i, len(nums)):\n            if nums[i] + nums[j] == target:\n                return [i, j]",
  "language": "python",
  "request_type": "debug",
  "hint_level": 1
}
```

**Response Payload**:
```json
{
  "status": "success",
  "model_used": "gemini-2.5-flash",
  "response": {
    "status": "Incorrect",
    "diagnosis": "The code allows using the same array element twice when i equals j.",
    "explanation": "Starting the inner loop at i rather than i + 1 means nums[i] can pair with itself.",
    "hint": "Check the inner loop start boundary. Can an element at index i be used twice?",
    "concept": "Nested Loop Indexing",
    "pattern": "Hash Map Optimization",
    "complexity_feedback": "Current time complexity is O(N^2). Consider using a Hash Map for O(N).",
    "next_action": "Change inner loop to range(i + 1, len(nums)).",
    "error_line": 3,
    "error_type": "LogicError",
    "hint_level": 1,
    "should_show_solution": false,
    "confidence": 0.92,
    "sources": [
      {
        "chunk_id": "a1b2c3d4-...",
        "title": "Two Sum - Common Mistakes",
        "topic": "Arrays",
        "pattern": "Hash Map",
        "chunk_type": "mistakes",
        "score": 0.85,
        "snippet": "Avoid using the same element index twice..."
      }
    ]
  },
  "retrieved_chunks": 3,
  "sources": [ ... ],
  "token_usage": {
    "prompt_tokens": 420,
    "completion_tokens": 180,
    "total_tokens": 600,
    "latency_ms": 1150
  }
}
```

---

## 13. Project Directory Structure

```
CodeSpyde/
├── app.py                      # Main Streamlit frontend application entry point
├── backend/                    # FastAPI backend codebase
│   ├── app.py                  # FastAPI application & startup event initialization
│   ├── config.py               # Environment configuration loader (.env)
│   ├── database.py             # PostgreSQL connection pool and transaction context managers
│   ├── requirements.txt        # Backend Python dependencies
│   ├── agent/                  # LangGraph agent implementation
│   │   ├── graph.py            # StateGraph builder and compiled graph instance
│   │   ├── nodes.py            # Individual graph node functions (13 nodes)
│   │   ├── routing.py          # Conditional edge decision routers
│   │   ├── state.py            # DSAAgentState TypedDict definition
│   │   └── prompts.py          # Agent-specific prompt templates
│   ├── embeddings/             # Embedding generation service
│   │   └── gemini_embeddings.py# Google Gemini Embeddings API wrapper
│   ├── ingestion/              # Data ingestion pipeline
│   │   ├── cleaner.py          # Document cleaning and normalization
│   │   ├── chunker.py          # Semantic section-based chunking logic
│   │   ├── metadata.py         # Metadata extractor
│   │   ├── loader.py           # JSON file loader
│   │   └── ingest.py           # Ingestion script populating PostgreSQL/pgvector
│   ├── models/                 # Pydantic data schemas
│   │   └── schemas.py          # API request, response, and CoachAIResponse schemas
│   ├── rag/                    # RAG pipeline management
│   │   ├── pipeline.py         # End-to-end RAG orchestrator (run_coach_rag)
│   │   ├── context_builder.py  # Context string formatter for LLM prompt
│   │   └── prompts.py          # System and user coach prompt builders
│   ├── retrieval/              # Vector, Keyword, Hybrid, and Reranking search
│   │   ├── vector_search.py    # pgvector HNSW cosine similarity search
│   │   ├── keyword_search.py   # PostgreSQL full-text search (tsvector/GIN)
│   │   ├── hybrid_search.py    # Hybrid search fusing results via RRF
│   │   ├── reranker.py         # SentenceTransformers Cross-Encoder reranker
│   │   └── retriever.py        # High-level retrieval pipeline interface
│   ├── routes/                 # FastAPI API route handlers
│   │   ├── coach.py            # Main /api/coach endpoint
│   │   ├── code.py             # /api/code/analyze and /api/code/execute endpoints
│   │   ├── problems.py         # /api/problems problem registry endpoints
│   │   └── rag.py              # /api/rag/search direct search endpoint
│   ├── services/               # Core execution and business services
│   │   ├── ai_coach.py         # Gemini API client & response generator
│   │   ├── code_analyzer.py    # AST static Python analyzer
│   │   ├── code_executor.py    # Subprocess runner & test case harness
│   │   ├── student_history.py  # Student attempt persistence service
│   │   └── token_tracker.py    # Token telemetry and latency logging service
│   └── sql/                    # SQL database schemas
│       └── schema.sql          # Table definitions, pgvector extension, and indexes
├── data/                       # Knowledge base JSON datasets
│   ├── concepts/               # Data structure concepts JSON files
│   ├── examples/               # Example execution traces JSON files
│   ├── mistakes/               # Common student mistakes JSON files
│   ├── patterns/               # Algorithmic patterns JSON files
│   ├── problems/               # Problem definitions JSON files
│   └── solutions/              # Optimal solutions JSON files
├── frontend/                   # Streamlit components and UI assets
│   ├── api_client.py           # REST client wrapper interfacing with FastAPI
│   ├── config.py               # Frontend configuration (API_BASE_URL)
│   ├── diagnostics.py          # Health diagnostic utilities
│   ├── styles.py               # Custom CSS design system and theme styles
│   └── components/             # Reusable UI component modules
│       ├── bottom_panel.py     # Output console, test results & AI coach panel
│       ├── editor.py           # Code editor integration
│       ├── header.py           # Problem header and metadata bar
│       ├── problem_view.py     # Problem description renderer
│       └── sidebar.py          # Problem selection & navigation sidebar
└── scripts/                    # Verification and validation scripts
    ├── validate_dataset.py     # Dataset integrity & JSON syntax validator
    ├── validate_project.py     # Project subsystem & offline scenario verifier
    └── verify_live.py          # End-to-end live pipeline verification suite
```

---

## 14. Installation Setup Guide

Follow these step-by-step instructions to set up and run the project locally.

### Prerequisites
- **Python**: Version 3.10 or higher installed.
- **PostgreSQL**: Version 15 or higher installed with `pgvector` extension enabled.
- **Google Gemini API Key**: Valid API key from [Google AI Studio](https://aistudio.google.com/).

### 1. Clone Repository
```bash
git clone https://github.com/preeti-priyanka77/ITER-Cohort-Project.git
cd ITER-Cohort-Project/CodeSpyde
```

### 2. Create and Activate Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r backend/requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the `backend/` directory (or use `backend/.env`):
```bash
cp backend/.env.example backend/.env
```

Edit `backend/.env` with your database credentials and API key:
```env
APP_NAME="AI DSA Coach"
APP_VERSION="2.0.0"
DEBUG=true

# Database Connection String
DATABASE_URL=postgresql://postgres:password@localhost:5432/dsa_coach
LANGGRAPH_DATABASE_URL=postgresql://postgres:password@localhost:5432/dsa_coach

# Gemini API Configuration
GEMINI_API_KEY=your_actual_gemini_api_key_here
GEMINI_FAST_MODEL=gemini-2.5-flash
GEMINI_DEBUGGER_MODEL=gemini-2.5-flash
GEMINI_COACH_MODEL=gemini-2.5-flash
GEMINI_EMBEDDING_MODEL=models/gemini-embedding-001
EMBEDDING_DIMENSION=768

# RAG & Reranker Settings
RAG_ENABLED=true
RERANKER_ENABLED=true
RERANKER_MODEL=BAAI/bge-reranker-v2-m3
```

### 5. Configure PostgreSQL & Enable pgvector
Create the database and enable extensions in PostgreSQL:
```sql
CREATE DATABASE dsa_coach;
\c dsa_coach;
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS pgcrypto;
```

### 6. Initialize Database Schema
Execute the SQL schema to create tables and indexes:
```bash
# Using psql CLI
psql -U postgres -d dsa_coach -f backend/sql/schema.sql

# Alternatively, the backend automatically runs schema.sql idempotently on startup!
```

### 7. Run Dataset Ingestion Pipeline
Ingest the JSON knowledge base into PostgreSQL/pgvector:
```bash
python backend/ingestion/ingest.py
```

---

## 15. Running the Application

### 1. Start FastAPI Backend
From the root directory:
```bash
# Navigate to backend or set PYTHONPATH
cd backend
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```
*The backend will be available at `http://localhost:8000`. API documentation (Swagger UI) will be accessible at `http://localhost:8000/docs`.*

### 2. Start Streamlit Frontend
In a separate terminal window (with virtual environment activated):
```bash
# Run Streamlit from project root
streamlit run app.py
```
*The web UI will open automatically in your browser at `http://localhost:8501`.*

---

## 16. Testing & Validation

The project provides three automated verification scripts under `scripts/`:

### 1. Dataset Validation Script
Validates JSON formatting, schema required fields, unique document IDs, solution-to-problem reference integrity, and Python AST syntax within code fields:
```bash
python scripts/validate_dataset.py
```

### 2. Offline Subsystem & Scenario Validation
Validates imports, database connections, table schemas, mock embeddings, hybrid retrieval, cross-encoder reranking, and 5 core LangGraph agent execution scenarios:
```bash
python scripts/validate_project.py
```

### 3. Live End-to-End System Verification Suite
Performs full live verification including PostgreSQL connection, pgvector status, RAG pipeline, live LangGraph scenarios, real Gemini API structured response verification, student memory persistence, and Streamlit file presence:
```bash
python scripts/verify_live.py
```

---

## 17. Error Handling Strategy

| Error Category | Root Cause | System Response & Mitigation |
|---|---|---|
| **Syntax Error** | Invalid Python code syntax | Detected via `ast.parse()` before execution. Bypasses execution subprocess and RAG, routing directly to Gemini to highlight exact line number and fix hint. |
| **Runtime Exception** | Uncaught exception (`IndexError`, `ZeroDivisionError`, etc.) | Subprocess captures `stderr` traceback. Routes through RAG hybrid search and Gemini debugger model to explain why exception occurred. |
| **Timeout Error** | Infinite loop or $O(N!)$ recursion | Process killed after 3 seconds (`CODE_EXECUTION_TIMEOUT`). Agent flags `timed_out: true` and hints student on iteration limits and loop boundaries. |
| **Wrong Answer** | Code runs cleanly but fails test assertions | Harness compares actual vs expected JSON output. Triggers RAG retrieval for algorithm patterns and provides progressive hints. |
| **Gemini API Limits** | Rate limit or quota exhaustion | Handled via try-except blocks; returns structured fallback error messages without crashing backend server. |
| **Database Failure** | PostgreSQL connection offline | `student_attempts` and `token_usage` saves fail gracefully with log warnings while AI Coach returns response to student uninterrupted. |

---

## 18. Security Considerations

- **Environment Key Isolation**: Sensitive parameters (`GEMINI_API_KEY`, `DATABASE_URL`) are strictly loaded via `python-dotenv` and ignored in Git commits.
- **Code Execution Sandbox**: Code execution runs in isolated Python subprocesses with restricted execution time (3s timeout) and maximum output size constraints (10,000 bytes) to prevent resource exhaustion attacks.
- **SQL Injection Prevention**: All database queries utilize parameterized queries (`%s` placeholders via `psycopg2`) preventing SQL injection.
- **Input Validation**: All incoming requests are parsed and sanitized using Pydantic models with strict field validation.

---

## 19. System Limitations

- **Language Support**: Code analysis (AST) and test-case execution currently support **Python**. Non-Python languages receive static notice fallbacks.
- **Subprocess Isolation**: Subprocess execution enforces strict timeouts and output limits, but does not currently run inside isolated Docker container sandboxes.
- **API Dependency**: Real-time AI coaching and vector query embedding rely on active internet connectivity and valid Google Gemini API quotas.

---

## 20. Future Roadmap (Planned)

- [ ] **Multi-Language Sandbox**: Extend AST analysis and code execution to C++, Java, and JavaScript using Docker container isolation.
- [ ] **Expanded Knowledge Base**: Expand dataset coverage to advanced topics (Advanced DP, Segment Trees, Trie, Union-Find).
- [ ] **Adaptive Difficulty Engine**: Track student skill profiles over time to dynamically recommend problems matching learning progression.
- [ ] **Automatic Test Case Generator**: Generate edge-case test inputs automatically using Gemini LLM reasoning.

---

## 21. Technology Stack Summary

| Layer | Technology | Purpose |
|---|---|---|
| **Frontend UI** | Streamlit, HTML5, Custom Vanilla CSS | Interactive student coding workspace & responsive UI |
| **Backend API** | FastAPI, Uvicorn | High-performance asynchronous REST API framework |
| **Agent Framework** | LangGraph, LangChain Core | Stateful agent flow orchestration & conditional routing |
| **Database & Vector Search** | PostgreSQL 15+, pgvector | Relational database with HNSW vector cosine search & GIN full-text search |
| **LLM & Embeddings** | Google Gemini API (`google-genai`) | Dense vector embedding generation & structured Socratic AI coaching |
| **Reranker Model** | SentenceTransformers (`BAAI/bge-reranker-v2-m3`) | Cross-Encoder transformer candidate re-ranking |
| **Static Code Analysis** | Python `ast` module | AST syntax error detection & column/line offset extraction |
| **Code Execution** | Python `subprocess`, `tempfile` | Isolated code execution runner with timeout handling |
| **Data Processing** | NumPy, Pandas, Pydantic | Data manipulation, schema validation, and numerical operations |
| **Verification & Testing** | Python `subprocess`, `sys`, Custom Test Suites | Automated dataset and multi-scenario system verification scripts |

---

# Complete Setup & Run on Another Machine

This section provides a complete, step-by-step guide to cloning, configuring, ingesting, and running the AI DSA Coach project on a fresh machine (Windows, Linux, or macOS).

---

### Quick Start

For experienced developers who want to get up and running immediately:

```bash
# 1. Clone & enter repository
git clone https://github.com/preeti-priyanka77/ITER-Cohort-Project.git
cd ITER-Cohort-Project/CodeSpyde

# 2. Setup Python environment
python -m venv venv
# Windows PowerShell: .\venv\Scripts\Activate.ps1
# Linux / macOS:     source venv/bin/activate
pip install -r backend/requirements.txt

# 3. Create & configure environment file
cp backend/.env.example backend/.env
# Edit backend/.env: Set GEMINI_API_KEY and DATABASE_URL

# 4. PostgreSQL setup (Run in psql)
# CREATE DATABASE dsa_coach;
# \c dsa_coach
# CREATE EXTENSION vector; CREATE EXTENSION pgcrypto;

# 5. Ingest Knowledge Base
python backend/ingestion/ingest.py

# 6. Start Backend (Terminal 1)
cd backend && uvicorn app:app --reload --host 0.0.0.0 --port 8000

# 7. Start Frontend (Terminal 2 from root)
streamlit run app.py
```

---

## 1. System Requirements

### REQUIRED
- **Operating Systems**: Windows 10/11, Linux (Ubuntu 20.04+ / Debian), macOS 12+ (Intel / Apple Silicon).
- **Python**: Version 3.10, 3.11, or 3.12.
- **PostgreSQL**: Version 15 or higher.
- **pgvector**: PostgreSQL vector similarity search extension (`0.5.0+`).
- **Git**: For repository cloning and version control.
- **Google Gemini API Key**: Active API key from [Google AI Studio](https://aistudio.google.com/).

### OPTIONAL
- **PyTorch with CUDA**: GPU support for `sentence-transformers` Cross-Encoder reranking (CPU execution is default and fully functional).
- **Node.js / Docker**: Not required. The system runs completely natively via Python subprocesses and PostgreSQL.

---

## 2. Clone the Project

Execute the following commands to clone the codebase:

```bash
git clone https://github.com/preeti-priyanka77/ITER-Cohort-Project.git
cd ITER-Cohort-Project/CodeSpyde
```

---

## 3. Python Environment

Create a virtual environment to isolate project dependencies:

### Windows (PowerShell)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Linux / macOS (Bash / Zsh)
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
```bash
pip install --upgrade pip
pip install -r backend/requirements.txt
```

---

## 4. Environment Variables

Create the `.env` file in the `backend/` directory:

```bash
# Copy template
cp backend/.env.example backend/.env
```

### Configuration Parameters Reference

| Variable | Requirement | Default / Recommended Value | Description |
|---|---|---|---|
| `APP_NAME` | REQUIRED | `AI DSA Coach` | Application identity header |
| `APP_VERSION` | REQUIRED | `2.0.0` | Application release version |
| `DEBUG` | REQUIRED | `true` | Toggle FastAPI debug logging |
| `DATABASE_URL` | REQUIRED | `postgresql://postgres:password@localhost:5432/dsa_coach` | Main PostgreSQL connection string |
| `LANGGRAPH_DATABASE_URL` | REQUIRED | `postgresql://postgres:password@localhost:5432/dsa_coach` | Checkpoint PostgreSQL connection string |
| `GEMINI_API_KEY` | REQUIRED | `your_actual_gemini_api_key` | Google Gemini API secret key |
| `GEMINI_FAST_MODEL` | REQUIRED | `gemini-2.5-flash` | Lightweight route for syntax error feedback |
| `GEMINI_DEBUGGER_MODEL` | REQUIRED | `gemini-2.5-flash` | Debugger route for execution error analysis |
| `GEMINI_COACH_MODEL` | REQUIRED | `gemini-2.5-flash` | Primary Socratic coaching LLM route |
| `GEMINI_EMBEDDING_MODEL` | REQUIRED | `models/gemini-embedding-001` | RAG vector embedding model |
| `EMBEDDING_DIMENSION` | REQUIRED | `768` | Vector dimensionality (must match pgvector schema) |
| `PYTHON_EXECUTABLE` | OPTIONAL | `python` | Subprocess Python binary name |
| `CODE_EXECUTION_TIMEOUT` | OPTIONAL | `3` | Execution process timeout in seconds |
| `MAX_OUTPUT_LENGTH` | OPTIONAL | `10000` | Truncation limit for stdout/stderr (characters) |
| `RAG_ENABLED` | OPTIONAL | `true` | Enable/disable RAG retrieval pipeline |
| `VECTOR_SEARCH_LIMIT` | OPTIONAL | `20` | Candidate limit for vector retrieval |
| `KEYWORD_SEARCH_LIMIT` | OPTIONAL | `20` | Candidate limit for tsvector keyword search |
| `HYBRID_SEARCH_LIMIT` | OPTIONAL | `15` | Candidate limit after RRF fusion |
| `RERANKER_MODEL` | OPTIONAL | `BAAI/bge-reranker-v2-m3` | Cross-Encoder model path |
| `RERANKER_ENABLED` | OPTIONAL | `true` | Enable/disable Cross-Encoder reranking |
| `RERANK_LIMIT` | OPTIONAL | `8` | Top candidate count passed to reranker |
| `FINAL_CONTEXT_LIMIT` | OPTIONAL | `6` | Max chunks injected into final LLM prompt |
| `STUDENT_MEMORY_ENABLED` | OPTIONAL | `true` | Enable PostgreSQL student attempt tracking |
| `TOKEN_TRACKING_ENABLED` | OPTIONAL | `true` | Enable token telemetry logging |
| `API_HOST` | OPTIONAL | `0.0.0.0` | FastAPI server bind address |
| `API_PORT` | OPTIONAL | `8000` | FastAPI server listening port |
| `STREAMLIT_API_URL` | OPTIONAL | `http://localhost:8000` | Frontend backend target URL |

---

## 5. Gemini API Setup

1. **Obtain API Key**: Visit [Google AI Studio](https://aistudio.google.com/) and generate an API key.
2. **Add Key to `.env`**: Set `GEMINI_API_KEY=your_key_here` in `backend/.env`.
3. **Model Customization**: Logical model routes (`GEMINI_FAST_MODEL`, `GEMINI_DEBUGGER_MODEL`, `GEMINI_COACH_MODEL`) are configurable without code edits. If you have access to newer models (e.g. `gemini-3.6-flash`), update these values in `backend/.env`.
4. **API Key Verification**: Verify API functionality via Python:
   ```bash
   python -c "from google import genai; import os; from dotenv import load_dotenv; load_dotenv('backend/.env'); client = genai.Client(api_key=os.getenv('GEMINI_API_KEY')); print('Gemini Client OK')"
   ```

---

## 6. PostgreSQL Setup

### Step 1: Create Database and User
Open `psql` or pgAdmin:
```sql
CREATE DATABASE dsa_coach;
-- Create user if needed:
-- CREATE USER postgres WITH PASSWORD 'password';
-- GRANT ALL PRIVILEGES ON DATABASE dsa_coach TO postgres;
```

### Step 2: Enable Database Extensions
Connect to `dsa_coach` and enable `vector` and `pgcrypto`:
```sql
\c dsa_coach;
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS pgcrypto;
```

### Step 3: Run Schema Initialization
Execute the project schema script:
```bash
psql -U postgres -d dsa_coach -f backend/sql/schema.sql
```
*Note: The FastAPI application also automatically runs `schema.sql` idempotently on startup!*

### Step 4: Verify Database Tables
Confirm that all 4 required tables exist:
```sql
\dt
-- Expected Output:
-- dsa_documents
-- dsa_chunks
-- student_attempts
-- token_usage
```

---

## 7. Knowledge Base & Ingestion Setup

The knowledge base dataset is located in the `data/` directory:
- `data/concepts/*.json`
- `data/patterns/*.json`
- `data/problems/*.json`
- `data/solutions/*.json`
- `data/mistakes/*.json`
- `data/examples/*.json`

### First-Time Knowledge Base Setup

Run the ingestion script to clean, chunk, generate embeddings, and load documents into PostgreSQL:

```bash
python backend/ingestion/ingest.py
```

```
data/ (JSON) ──> Cleaner ──> Chunker ──> Gemini Embedding API ──> PostgreSQL (dsa_documents & dsa_chunks)
```

### Safe Ingestion Resume & Quota Protection
- The ingestion script calculates a SHA-256 `content_hash` for each document.
- Documents already present in `dsa_documents` are automatically skipped.
- If ingestion is interrupted by API rate limits, **simply rerun `python backend/ingestion/ingest.py`**. It will safely resume without re-embedding existing documents or consuming duplicate quota.

---

## 8. Start Backend

Run the FastAPI Uvicorn dev server from the `backend/` directory:

```bash
cd backend
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

- **Host**: `0.0.0.0`
- **Port**: `8000`
- **Health Check Endpoint**: `http://localhost:8000/health`
- **API Documentation**: `http://localhost:8000/docs`

### Verify Backend Health
In another terminal:
```bash
curl http://localhost:8000/health
# Response: {"status":"healthy"}
```

---

## 9. Start Streamlit Frontend

Run the Streamlit interface from the project root directory:

```bash
# Ensure you are at the project root: ITER-Cohort-Project/CodeSpyde
streamlit run app.py
```

- **Local URL**: `http://localhost:8501`
- **Backend Connectivity**: The frontend connects to `API_BASE_URL` defined in `frontend/config.py` (default `http://localhost:8000`).
- **Initial View**: Streamlit will launch a wide-layout interactive workspace displaying the problem list, code editor, and console.

---

## 10. Complete Startup Order

For a fresh boot, follow this sequence:

1. **Start PostgreSQL Service**: Ensure PostgreSQL 15+ is running.
2. **Verify Database Extensions**: Ensure `vector` and `pgcrypto` exist in `dsa_coach`.
3. **Activate Python Environment**: `source venv/bin/activate` or `.\venv\Scripts\Activate.ps1`.
4. **Verify Configuration**: Ensure `backend/.env` exists and contains valid credentials.
5. **Run Knowledge Base Ingestion**: `python backend/ingestion/ingest.py` (first time or updates).
6. **Start FastAPI Backend**: `cd backend && uvicorn app:app --reload --port 8000`.
7. **Verify Health Probe**: Check `http://localhost:8000/health`.
8. **Start Streamlit Frontend**: Run `streamlit run app.py` from root.
9. **Open Browser**: Access `http://localhost:8501`.
10. **Select Problem**: Choose a problem (e.g., "Two Sum") from the sidebar.
11. **Edit Code**: Enter solution code in the editor.
12. **Execute & Coach**: Click **Run Code** to run tests, or **Ask AI Coach** for Socratic hints.

---

## 11. Verify Installation

Run the project's built-in validation suite to verify all components:

### 1. Validate Dataset Integrity
```bash
python scripts/validate_dataset.py
```
*Validates JSON structure, unique IDs, reference integrity, and Python syntax.*

### 2. Validate Offline Subsystems & Scenarios
```bash
python scripts/validate_project.py
```
*Validates database tables, mock embeddings, hybrid retrieval, reranker, and 5 LangGraph agent scenarios.*

### 3. Validate Live System Pipeline
```bash
python scripts/verify_live.py
```
*Verifies database, live Gemini API integration, memory, token tracking, and FastAPI handlers.*

**Expected Output**:
```
PROJECT STATUS: COMPLETE (ALL CHECKS PASSED)
```

---

## 12. End-to-End Verification Test

Perform this 12-step verification test on the running application:

1. Open `http://localhost:8501` in your browser.
2. Select **Two Sum** from the sidebar problem selector.
3. Replace the editor code with an intentionally bugged solution:
   ```python
   def solution(nums, target):
       for i in range(len(nums)):
           for j in range(i, len(nums)):
               if nums[i] + nums[j] == target:
                   return [i, j]
   ```
4. Click **Run Code**.
5. Observe execution output: Status shows failed cases (reuses index 0 when `nums[0] + nums[0] == target`).
6. Click **Ask AI Coach**.
7. Observe AI Coach Diagnosis: Identifies index duplication bug without spoiling full code.
8. Check Progressive Hint: Review Level 1 hint guiding loop bound adjustment.
9. Inspect Sources: Expand the RAG sources accordion to verify retrieved DSA knowledge chunks.
10. Correct the solution in the code editor:
    ```python
    def solution(nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in lookup:
                return [lookup[diff], i]
            lookup[num] = i
        return []
    ```
11. Click **Submit Code**.
12. Observe Acceptance: Status updates to **Accepted! All tests passed.** with time/space complexity analysis ($O(N)$ time, $O(N)$ space).

---

## 13. Troubleshooting Guide

| Problem | Likely Cause | Practical Fix |
|---|---|---|
| `could not connect to server: Connection refused` | PostgreSQL service is not running | Start PostgreSQL service (`services.msc` on Windows or `sudo service postgresql start` on Linux). |
| `type "vector" does not exist` | `pgvector` extension not installed | Run `CREATE EXTENSION vector;` in PostgreSQL `dsa_coach` database. |
| `RuntimeError: GEMINI_API_KEY is not configured` | Missing or empty key in `backend/.env` | Add valid key to `GEMINI_API_KEY=` inside `backend/.env`. |
| `429 Resource Has Been Exhausted` | Gemini API rate limit exceeded | Wait 60 seconds for quota reset or switch model in `.env` to `gemini-2.5-flash`. |
| `address already in use` (Port 8000 or 8501) | Another process is using port 8000 or 8501 | Kill process using port or run uvicorn on `--port 8001` and update `STREAMLIT_API_URL`. |
| `FastAPI Backend is unreachable at http://localhost:8000` | FastAPI server not started | Start uvicorn server via `cd backend && uvicorn app:app --reload`. |
| `ModuleNotFoundError: No module named 'fastapi'` | Virtual environment not activated | Activate virtual environment (`.\venv\Scripts\Activate.ps1` or `source venv/bin/activate`). |
| `Table "dsa_chunks" does not exist` | Schema not initialized | Run `psql -U postgres -d dsa_coach -f backend/sql/schema.sql` or restart FastAPI. |
| `0 chunks retrieved` | Ingestion script was not run | Run `python backend/ingestion/ingest.py` to populate knowledge base. |

---

## 14. Common Windows Issues & Solutions

### 1. PowerShell Script Execution Policy Error
If activating the virtual environment fails with `cannot be loaded because running scripts is disabled`:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 2. Command Prompt vs PowerShell Activation
- **PowerShell**: `.\venv\Scripts\Activate.ps1`
- **Command Prompt (cmd.exe)**: `venv\Scripts\activate.bat`

### 3. Python Executable Resolution
If `python` defaults to the Windows Store installer, set `PYTHON_EXECUTABLE` in `backend/.env` to your full Python binary path:
```env
PYTHON_EXECUTABLE=C:\Python310\python.exe
```

---

## 15. Project Run Modes

### Development Mode (Default)
Enables live reload, verbose logging, and Streamlit auto-rerun:
- **Backend**: `cd backend && uvicorn app:app --reload --host 0.0.0.0 --port 8000`
- **Config**: `DEBUG=true` in `backend/.env`.

### Production-like Local Run
For performance testing without reload overhead:
- **Backend**: `cd backend && uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4`
- **Config**: `DEBUG=false` in `backend/.env`.

---

## 16. New Machine Reproducibility Checklist

- [ ] Git installed and repository cloned
- [ ] Python 3.10+ installed
- [ ] PostgreSQL 15+ installed and running
- [ ] `pgvector` extension enabled in `dsa_coach` database
- [ ] Python virtual environment created and activated
- [ ] Dependencies installed via `pip install -r backend/requirements.txt`
- [ ] `backend/.env` file created from `.env.example`
- [ ] Valid `GEMINI_API_KEY` configured in `.env`
- [ ] PostgreSQL connection string `DATABASE_URL` configured in `.env`
- [ ] `schema.sql` executed / database tables verified
- [ ] Data ingestion script `python backend/ingestion/ingest.py` completed
- [ ] FastAPI backend running at `http://localhost:8000`
- [ ] Health check `http://localhost:8000/health` returning `{"status": "healthy"}`
- [ ] Streamlit frontend running at `http://localhost:8501`
- [ ] Validation scripts passed (`validate_dataset.py`, `validate_project.py`, `verify_live.py`)
- [ ] End-to-end bugged and accepted solution test completed successfully

