from langchain_community.document_loaders import TextLoader
from sqlalchemy import text
from db import engine
from model import embeddings
from chunking import chunk_text
import os

def process_txt(filename):

    # Step 1: Load the knowledge-base file
    loader = TextLoader(filename, encoding="utf-8")
    docs = loader.load()

    text_content = docs[0].page_content

    # Step 2: Use the selected chunking strategy
    chunks_dict = chunk_text(text_content)

    # TokenTextSplitter was selected based on evaluation
    chunks = chunks_dict["token"]

    print(f"\nUsing TokenTextSplitter")
    print(f"Number of chunks: {len(chunks)}")

    # Step 3: Insert chunks and embeddings into PostgreSQL
    with engine.connect() as conn:

        for i, chunk in enumerate(chunks):

            # Insert chunk into raw_documents
            result = conn.execute(
                text("""
                    INSERT INTO raw_documents
                    (filename, chunk_id, content)
                    VALUES (:filename, :chunk_id, :content)
                    RETURNING id
                """),
                {
                    "filename": filename,
                    "chunk_id": i,
                    "content": chunk
                }
            )

            # Get raw_documents.id
            raw_id = result.scalar()

            # Generate embedding
            vector = embeddings.embed_query(chunk)

            print(
                f"Chunk {i + 1}/{len(chunks)} "
                f"→ embedding dimension: {len(vector)}"
            )

            # Store embedding in pgvector
            conn.execute(
                text("""
                    INSERT INTO document_embeddings
                    (raw_id, embedding)
                    VALUES (:raw_id, :embedding)
                """),
                {
                    "raw_id": raw_id,
                    "embedding": vector
                }
            )

        # save the transaction
        conn.commit()

    print(
        f"\n✅ Loaded {len(chunks)} chunks from {filename}"
    )
    print("✅ Embeddings stored in PostgreSQL + pgvector")

# LOAD ALL KNOWLEDGE-BASE FILES
def load_knowledge_base(folder="knowledge_base"):

    print("\n" + "=" * 60)
    print("        LOADING KNOWLEDGE BASE")
    print("=" * 60)

    files = [
        file
        for file in os.listdir(folder)
        if file.lower().endswith((".txt", ".md"))
    ]

    print(f"\nFound {len(files)} files.")

    for file in files:

        filepath = os.path.join(folder, file)

        print("\n" + "-" * 60)
        print(f"Processing: {file}")
        print("-" * 60)

        try:
            process_txt(filepath)

        except Exception as e:
            print(f"❌ Error processing {file}: {e}")

    print("\n" + "=" * 60)
    print("        KNOWLEDGE BASE LOADING COMPLETE")
    print("=" * 60)


# RUN
if __name__ == "__main__":
    load_knowledge_base()