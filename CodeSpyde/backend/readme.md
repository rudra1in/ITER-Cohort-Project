╔══════════════════════════════════════════════════════╗
║                  DSA KNOWLEDGE                       ║
╚══════════════════════════════════════════════════════╝
                         │
                         ▼
                  Document Loader
                         │
                         ▼
              Cleaning / Normalization
                         │
                         ▼
                  DSA Chunking
                         │
                         ▼
                  Metadata Layer
                         │
                         ▼
                Gemini Embeddings
                         │
                         ▼
               PostgreSQL + pgvector
                         │
               ┌─────────┴─────────┐
               ▼                   ▼
          Vector Search       Keyword Search
               │                   │
               └─────────┬─────────┘
                         ▼
                    RRF HYBRID
                         │
                         ▼
                  CROSS ENCODER
                    RERANKER
                         │
                         ▼
                       TOP-K
                         │
       ┌─────────────────┼─────────────────┐
       ▼                 ▼                 ▼
  Problem Context   Student Code     Execution Result
       │                 │                 │
       └─────────────────┼─────────────────┘
                         ▼
                  CONTEXT BUILDER
                         │
                         ▼
                   MODEL ROUTER
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
       COACH          DEBUGGER         FAST
       MODEL           MODEL           MODEL
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                 STRUCTURED OUTPUT
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
    Error Line       Explanation        Hint
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                   MONACO EDITOR
                         │
                         ▼
                  Student retries
                         │
                         ▼
                 Student History
                         │
                         └───────────────► RAG