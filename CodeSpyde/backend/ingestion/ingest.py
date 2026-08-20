import hashlib
import json
import time
import random
from pathlib import Path

from database import get_db_cursor

from embeddings.gemini_embeddings import (
    create_embedding
)

from ingestion.cleaner import (
    clean_document
)

from ingestion.chunker import (
    create_dsa_chunks
)

from ingestion.loader import (
    load_directory
)

from ingestion.metadata import (
    extract_metadata
)


# =========================================================
# RATE LIMITER & RETRIES
# =========================================================

class RateLimiter:
    def __init__(self, requests_per_minute: int = 60):
        self.delay = 60.0 / requests_per_minute
        self.last_request_time = 0.0

    def wait(self):
        elapsed = time.time() - self.last_request_time
        if elapsed < self.delay:
            time.sleep(self.delay - elapsed)
        self.last_request_time = time.time()

limiter = RateLimiter(requests_per_minute=60) # Safely below the 100 RPM limit

def create_embedding_with_retry(text: str, max_retries: int = 5) -> list[float]:
    retries = 0
    delay = 2.0
    while True:
        try:
            limiter.wait()
            return create_embedding(text)
        except Exception as e:
            err_str = str(e).lower()
            if "429" in err_str or "resource_exhausted" in err_str or "quota" in err_str:
                retries += 1
                if retries > max_retries:
                    raise RuntimeError(f"Max retries reached for embedding API. Last error: {e}") from e
                sleep_time = delay * (2 ** (retries - 1)) + random.uniform(0, 1.0)
                print(f"    [RETRIED] Embedding 429 received. Sleeping {sleep_time:.2f}s before retry {retries}/{max_retries}...")
                time.sleep(sleep_time)
            else:
                raise



# =========================================================
# HELPERS
# =========================================================

def calculate_hash(
    document: dict
) -> str:

    serialized = json.dumps(
        document,
        sort_keys=True,
        ensure_ascii=False,
        default=str
    )

    return hashlib.sha256(
        serialized.encode("utf-8")
    ).hexdigest()


def estimate_token_count(
    text: str
) -> int:

    # Simple estimation.
    #
    # This is NOT the Gemini tokenizer.
    # It is only used as lightweight metadata.
    #
    # Actual API token usage should be recorded
    # from the model response metadata.

    if not text:
        return 0

    return max(
        1,
        len(text) // 4
    )


# =========================================================
# DOCUMENT INSERTION
# =========================================================

def insert_document(
    cursor,
    document: dict,
    content_hash: str
):

    cursor.execute(
        """
        INSERT INTO dsa_documents
        (
            title,
            source,
            document_type,
            topic,
            subtopic,
            pattern,
            difficulty,
            language,
            metadata,
            content_hash
        )
        VALUES
        (
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s
        )
        ON CONFLICT (content_hash)
        DO UPDATE SET
            updated_at = CURRENT_TIMESTAMP
        RETURNING id
        """,
        (
            document.get(
                "title",
                "Untitled"
            ),

            document.get(
                "source"
            ) or document.get(
                "_source_file"
            ),

            document.get(
                "document_type",
                "dsa"
            ),

            document.get(
                "topic"
            ),

            document.get(
                "subtopic"
            ),

            document.get(
                "pattern"
            ),

            document.get(
                "difficulty"
            ),

            document.get(
                "language"
            ),

            json.dumps(
                document,
                ensure_ascii=False,
                default=str
            ),

            content_hash
        )
    )

    return cursor.fetchone()[0]


# =========================================================
# CHUNK INSERTION
# =========================================================

def insert_chunk(
    cursor,
    document_id,
    chunk,
    embedding
):

    cursor.execute(
        """
        INSERT INTO dsa_chunks
        (
            document_id,
            chunk_index,
            chunk_type,
            title,
            content,
            topic,
            subtopic,
            pattern,
            difficulty,
            code,
            language,
            time_complexity,
            space_complexity,
            source_reference,
            token_count,
            embedding,
            metadata
        )
        VALUES
        (
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,
            %s,%s
        )
        """,
        (
            document_id,

            chunk.chunk_index,

            chunk.chunk_type,

            chunk.title,

            chunk.content,

            chunk.topic,

            chunk.subtopic,

            chunk.pattern,

            chunk.difficulty,

            chunk.code,

            chunk.language,

            chunk.time_complexity,

            chunk.space_complexity,

            chunk.source_reference,

            estimate_token_count(
                chunk.content
            ),

            embedding,

            json.dumps(
                {
                    "chunk_type":
                        chunk.chunk_type,
                    "topic":
                        chunk.topic,
                    "pattern":
                        chunk.pattern
                }
            )
        )
    )


# =========================================================
# SINGLE DOCUMENT
# =========================================================

def ingest_document(
    document: dict
) -> dict:

    # -----------------------------------------------------
    # Clean
    # -----------------------------------------------------

    document = clean_document(
        document
    )

    # -----------------------------------------------------
    # Extract metadata
    # -----------------------------------------------------

    document = extract_metadata(
        document
    )

    # -----------------------------------------------------
    # Hash
    # -----------------------------------------------------

    content_hash = calculate_hash(
        document
    )

    # -----------------------------------------------------
    # Check if already successfully ingested
    # -----------------------------------------------------

    with get_db_cursor() as cursor:
        cursor.execute(
            "SELECT id FROM dsa_documents WHERE content_hash = %s",
            (content_hash,)
        )
        existing_doc = cursor.fetchone()
        if existing_doc:
            doc_id = existing_doc[0]
            cursor.execute(
                "SELECT count(*) FROM dsa_chunks WHERE document_id = %s",
                (doc_id,)
            )
            chunks_count = cursor.fetchone()[0]
            if chunks_count > 0:
                return {
                    "status": "skipped",
                    "reason": "Already exists with chunks in database.",
                    "title": document.get("title")
                }

    # -----------------------------------------------------
    # Create DSA chunks
    # -----------------------------------------------------

    chunks = create_dsa_chunks(
        document
    )

    if not chunks:

        return {
            "status": "skipped",
            "reason": "No usable content.",
            "title": document.get(
                "title"
            )
        }

    # -----------------------------------------------------
    # Database
    # -----------------------------------------------------

    with get_db_cursor() as cursor:

        document_id = insert_document(
            cursor,
            document,
            content_hash
        )

        # Remove old chunks if document
        # is being re-ingested.

        cursor.execute(
            """
            DELETE FROM dsa_chunks
            WHERE document_id = %s
            """,
            (document_id,)
        )

        # -------------------------------------------------
        # Generate + store embeddings
        # -------------------------------------------------

        for chunk in chunks:

            embedding_text = build_embedding_text(
                chunk
            )

            embedding = create_embedding_with_retry(
                embedding_text
            )

            insert_chunk(
                cursor,
                document_id,
                chunk,
                embedding
            )

    return {
        "status": "success",
        "title": document.get(
            "title"
        ),
        "document_id": str(
            document_id
        ),
        "chunks_created": len(
            chunks
        )
    }


# =========================================================
# EMBEDDING TEXT
# =========================================================

def build_embedding_text(
    chunk
) -> str:

    parts = [
        f"Topic: {chunk.topic}",
        f"Subtopic: {chunk.subtopic}",
        f"Pattern: {chunk.pattern}",
        f"Difficulty: {chunk.difficulty}",
        f"Chunk Type: {chunk.chunk_type}",
        f"Title: {chunk.title}",
        "",
        chunk.content
    ]

    return "\n".join(
        str(part)
        for part in parts
        if part is not None
    )


# =========================================================
# DIRECTORY INGESTION
# =========================================================

def ingest_directory(
    directory: str | Path
) -> dict:

    documents = load_directory(
        directory
    )

    results = []

    for index, document in enumerate(
        documents,
        start=1
    ):

        title = document.get("title", "Untitled")
        print(f"[{index}/{len(documents)}] {title}")

        try:

            result = ingest_document(document)
            results.append(result)

            status = result["status"]
            if status == "success":
                print(
                    f"    [SUCCESS] chunks={result.get('chunks_created', '?')}"
                )
            elif status == "skipped":
                print(
                    f"    [SKIPPED] {result.get('reason', '')}"
                )
            else:
                print(f"    [{status.upper()}]")

        except Exception as error:

            result = {
                "status": "failed",
                "title": title,
                "error": str(error)
            }
            results.append(result)
            print(f"    [FAILED] {error}")

    successful = sum(
        1 for r in results if r["status"] == "success"
    )
    failed = sum(
        1 for r in results if r["status"] == "failed"
    )
    skipped = sum(
        1 for r in results if r["status"] == "skipped"
    )

    print(
        f"\n--- Ingestion complete ---"
        f"\n  SUCCESS : {successful}"
        f"\n  SKIPPED : {skipped}"
        f"\n  FAILED  : {failed}"
        f"\n  TOTAL   : {len(results)}"
    )

    return {
        "total": len(results),
        "successful": successful,
        "failed": failed,
        "skipped": skipped,
        "results": results
    }


# =========================================================
# CLI
# =========================================================

if __name__ == "__main__":

    import sys

    if len(sys.argv) < 2:

        print(
            "Usage:"
        )

        print(
            "python -m ingestion.ingest "
            "../data"
        )

        raise SystemExit(1)

    directory = sys.argv[1]

    summary = ingest_directory(
        directory
    )

    print("\n")
    print(
        "================================"
    )
    print(
        "INGESTION COMPLETE"
    )
    print(
        "================================"
    )

    print(
        f"Documents: {summary['total']}"
    )

    print(
        f"Successful: {summary['successful']}"
    )

    print(
        f"Failed: {summary['failed']}"
    )

    print(
        f"Skipped: {summary['skipped']}"
    )