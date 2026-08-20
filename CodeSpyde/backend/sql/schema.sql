-- =========================================================
-- AI DSA COACH DATABASE
-- PART 2 - RAG INGESTION
-- =========================================================

CREATE EXTENSION IF NOT EXISTS vector;

CREATE EXTENSION IF NOT EXISTS pgcrypto;


-- =========================================================
-- DSA DOCUMENTS
-- =========================================================

CREATE TABLE IF NOT EXISTS dsa_documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    title TEXT NOT NULL,

    source TEXT,

    document_type VARCHAR(50) NOT NULL,

    topic VARCHAR(100),
    subtopic VARCHAR(100),
    pattern VARCHAR(100),

    difficulty VARCHAR(30),

    language VARCHAR(30),

    metadata JSONB DEFAULT '{}'::jsonb,

    content_hash VARCHAR(64) UNIQUE,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- =========================================================
-- DSA CHUNKS
-- =========================================================

CREATE TABLE IF NOT EXISTS dsa_chunks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    document_id UUID NOT NULL
        REFERENCES dsa_documents(id)
        ON DELETE CASCADE,

    chunk_index INTEGER NOT NULL,

    chunk_type VARCHAR(50) NOT NULL,

    title TEXT,

    content TEXT NOT NULL,

    topic VARCHAR(100),
    subtopic VARCHAR(100),
    pattern VARCHAR(100),

    difficulty VARCHAR(30),

    code TEXT,

    language VARCHAR(30),

    time_complexity VARCHAR(100),
    space_complexity VARCHAR(100),

    source_reference TEXT,

    token_count INTEGER,

    embedding VECTOR(768),

    metadata JSONB DEFAULT '{}'::jsonb,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- =========================================================
-- FULL TEXT SEARCH
-- =========================================================

ALTER TABLE dsa_chunks
ADD COLUMN IF NOT EXISTS search_vector tsvector;


-- =========================================================
-- POPULATE SEARCH VECTOR
-- =========================================================

UPDATE dsa_chunks
SET search_vector =
    to_tsvector(
        'english',
        COALESCE(title, '') || ' ' ||
        COALESCE(content, '') || ' ' ||
        COALESCE(topic, '') || ' ' ||
        COALESCE(subtopic, '') || ' ' ||
        COALESCE(pattern, '') || ' ' ||
        COALESCE(chunk_type, '')
    )
WHERE search_vector IS NULL;


-- =========================================================
-- INDEXES
-- =========================================================

CREATE INDEX IF NOT EXISTS
idx_dsa_chunks_document
ON dsa_chunks(document_id);


CREATE INDEX IF NOT EXISTS
idx_dsa_chunks_topic
ON dsa_chunks(topic);


CREATE INDEX IF NOT EXISTS
idx_dsa_chunks_subtopic
ON dsa_chunks(subtopic);


CREATE INDEX IF NOT EXISTS
idx_dsa_chunks_pattern
ON dsa_chunks(pattern);


CREATE INDEX IF NOT EXISTS
idx_dsa_chunks_difficulty
ON dsa_chunks(difficulty);


CREATE INDEX IF NOT EXISTS
idx_dsa_chunks_type
ON dsa_chunks(chunk_type);


CREATE INDEX IF NOT EXISTS
idx_dsa_chunks_search
ON dsa_chunks
USING GIN(search_vector);


-- =========================================================
-- VECTOR INDEX
-- =========================================================
--
-- HNSW is preferable for a modern pgvector setup.
--
-- This index is only useful after embeddings have been
-- inserted.
--

CREATE INDEX IF NOT EXISTS
idx_dsa_chunks_embedding
ON dsa_chunks
USING hnsw (embedding vector_cosine_ops);


-- =========================================================
-- STUDENT ATTEMPTS
-- =========================================================

CREATE TABLE IF NOT EXISTS student_attempts (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    user_id VARCHAR(100),

    problem_id VARCHAR(100) NOT NULL,

    code TEXT NOT NULL,

    language VARCHAR(30) NOT NULL,

    status VARCHAR(50),

    error_type VARCHAR(100),

    error_line INTEGER,

    error_message TEXT,

    attempts INTEGER DEFAULT 1,

    solved BOOLEAN DEFAULT FALSE,

    execution_result JSONB,

    coach_response JSONB,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- =========================================================
-- TOKEN USAGE
-- =========================================================

CREATE TABLE IF NOT EXISTS token_usage (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    user_id VARCHAR(100),

    problem_id VARCHAR(100),

    model_name VARCHAR(150) NOT NULL,

    request_type VARCHAR(100) NOT NULL,

    input_tokens INTEGER DEFAULT 0,

    output_tokens INTEGER DEFAULT 0,

    total_tokens INTEGER DEFAULT 0,

    retrieved_chunks INTEGER DEFAULT 0,

    latency_ms INTEGER,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- =========================================================
-- INDEXES
-- =========================================================

CREATE INDEX IF NOT EXISTS
idx_student_attempts_user
ON student_attempts(user_id);


CREATE INDEX IF NOT EXISTS
idx_student_attempts_problem
ON student_attempts(problem_id);


CREATE INDEX IF NOT EXISTS
idx_student_attempts_created
ON student_attempts(created_at);


CREATE INDEX IF NOT EXISTS
idx_token_usage_user
ON token_usage(user_id);


CREATE INDEX IF NOT EXISTS
idx_token_usage_model
ON token_usage(model_name);


CREATE INDEX IF NOT EXISTS
idx_token_usage_created
ON token_usage(created_at);