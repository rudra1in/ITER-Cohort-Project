from app.rag.loader import load_dsa_documents
from app.rag.metadata import merge_duplicate_problems
from app.rag.splitter import split_documents
from app.rag.embeddings import create_embedding_model


print("Loading documents...")

documents = load_dsa_documents()

print("Processing metadata...")

unique_documents = merge_duplicate_problems(documents)

print("Splitting documents...")

chunks = split_documents(unique_documents)

print(f"\nUnique problems: {len(unique_documents)}")
print(f"Total chunks: {len(chunks)}")


print("\nLoading embedding model...")

embedding_model = create_embedding_model()

print("Embedding first chunk...")

vector = embedding_model.embed_query(
    chunks[0].page_content
)


print("\n========== EMBEDDING TEST ==========")

print("Problem:", chunks[0].metadata["title"])
print("Section:", chunks[0].metadata["section"])
print("Vector dimensions:", len(vector))

print("\nFirst 10 values:")
print(vector[:10])