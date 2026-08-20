# ============================================================
# DSA KNOWLEDGE INGESTION
# PostgreSQL + pgvector
# ============================================================

from typing import List

from langchain_core.documents import Document

from app.rag.loader import load_dsa_documents
from app.rag.metadata import merge_duplicate_problems
from app.rag.splitter import split_documents
from app.rag.embeddings import create_embedding_model

from app.database.database import SessionLocal
from app.database.models import KnowledgeChunk


# ============================================================
# PREPARE DOCUMENTS
# ============================================================

def prepare_documents() -> List[Document]:
    """
    Load, enrich, and split the DSA knowledge base.

    Pipeline:

        Markdown files
            ↓
        Loader
            ↓
        Metadata processing
            ↓
        Semantic section splitting
            ↓
        Chunks
    """

    print()
    print("=== STEP 1: Loading DSA documents ===")

    documents = load_dsa_documents()

    print(
        f"Loaded {len(documents)} original documents."
    )

    print()
    print("=== STEP 2: Adding metadata ===")

    documents = merge_duplicate_problems(
        documents
    )

    print(
        "Unique problems after metadata processing: "
        f"{len(documents)}"
    )

    print()
    print("=== STEP 3: Splitting documents ===")

    chunks = split_documents(
        documents
    )

    print(
        f"Created {len(chunks)} semantic chunks."
    )

    return chunks


# ============================================================
# INGEST DOCUMENTS
# ============================================================

def ingest_documents():
    """
    Generate embeddings for all DSA chunks
    and store them in PostgreSQL + pgvector.
    """

    chunks = prepare_documents()

    if not chunks:

        print(
            "No documents found. Nothing to ingest."
        )

        return

    # --------------------------------------------------------
    # CREATE EMBEDDING MODEL
    # --------------------------------------------------------

    print()
    print(
        "=== STEP 4: Creating embedding model ==="
    )

    embedding_model = (
        create_embedding_model()
    )

    print(
        "Embedding model loaded."
    )

    # --------------------------------------------------------
    # GENERATE EMBEDDINGS
    # --------------------------------------------------------

    print()
    print(
        "=== STEP 5: Generating embeddings ==="
    )

    texts = [
        chunk.page_content
        for chunk in chunks
    ]

    embeddings = (
        embedding_model.embed_documents(
            texts
        )
    )

    print(
        f"Generated {len(embeddings)} embeddings."
    )

    # --------------------------------------------------------
    # VERIFY EMBEDDING DIMENSION
    # --------------------------------------------------------

    if embeddings:

        dimension = len(
            embeddings[0]
        )

        print(
            f"Embedding dimension: {dimension}"
        )

        if dimension != 384:

            raise ValueError(
                "Embedding dimension mismatch. "
                f"Expected 384, received {dimension}."
            )

    # --------------------------------------------------------
    # STORE IN POSTGRESQL
    # --------------------------------------------------------

    print()
    print(
        "=== STEP 6: Storing in PostgreSQL ==="
    )

    db = SessionLocal()

    try:

        # ----------------------------------------------------
        # Clear previous ingestion
        #
        # Useful during development because the script
        # can be safely executed again.
        # ----------------------------------------------------

        deleted_count = (
            db.query(
                KnowledgeChunk
            ).delete()
        )

        db.commit()

        print(
            f"Cleared {deleted_count} "
            "previous knowledge chunks."
        )

        # ----------------------------------------------------
        # INSERT CHUNKS
        # ----------------------------------------------------

        for index, (
            chunk,
            embedding,
        ) in enumerate(
            zip(
                chunks,
                embeddings,
            )
        ):

            metadata = chunk.metadata

            knowledge_chunk = KnowledgeChunk(

                problem_id=metadata.get(
                    "problem_id",
                    "unknown",
                ),

                title=metadata.get(
                    "title",
                    "Unknown Problem",
                ),

                topic=metadata.get(
                    "topic",
                    "unknown",
                ),

                difficulty=metadata.get(
                    "difficulty",
                    "unknown",
                ),

                pattern=metadata.get(
                    "pattern",
                    "unknown",
                ),

                section=metadata.get(
                    "section",
                    "unknown",
                ),

                content=chunk.page_content,

                source=metadata.get(
                    "source",
                ),

                embedding=embedding,
            )

            db.add(
                knowledge_chunk
            )

            # ------------------------------------------------
            # Progress
            # ------------------------------------------------

            if (
                (index + 1) % 50 == 0
                or index + 1 == len(chunks)
            ):

                print(
                    f"Stored "
                    f"{index + 1}/"
                    f"{len(chunks)} chunks..."
                )

        # ----------------------------------------------------
        # COMMIT
        # ----------------------------------------------------

        db.commit()

        print()
        print(
            "======================================"
        )

        print(
            "INGESTION COMPLETED SUCCESSFULLY"
        )

        print(
            "======================================"
        )

        print(
            f"Total chunks stored: "
            f"{len(chunks)}"
        )

    except Exception as error:

        db.rollback()

        print()
        print(
            "ERROR DURING INGESTION:"
        )

        print(
            error
        )

        raise

    finally:

        db.close()


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    ingest_documents()