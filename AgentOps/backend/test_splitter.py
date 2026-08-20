from app.rag.loader import load_dsa_documents
from app.rag.metadata import merge_duplicate_problems
from app.rag.splitter import split_documents


# Load all Markdown files
documents = load_dsa_documents()

# Add metadata and remove duplicates
unique_documents = merge_duplicate_problems(documents)

# Split into semantic chunks
chunks = split_documents(unique_documents)


print("\n========== SPLITTER TEST ==========")

print(f"Original files: {len(documents)}")
print(f"Unique problems: {len(unique_documents)}")
print(f"Total chunks: {len(chunks)}")


print("\n========== FIRST 10 CHUNKS ==========")

for index, chunk in enumerate(chunks[:10]):

    print("\n-----------------------------------")
    print(f"Chunk #{index + 1}")

    print("Problem ID:")
    print(chunk.metadata.get("problem_id"))

    print("Title:")
    print(chunk.metadata.get("title"))

    print("Section:")
    print(chunk.metadata.get("section"))

    print("Section Title:")
    print(chunk.metadata.get("section_title"))

    print("\nContent:")
    print(chunk.page_content[:500])