from app.rag.loader import load_dsa_documents


documents = load_dsa_documents()

print("\n========== TEST RESULT ==========")
print(f"Total documents loaded: {len(documents)}")

if documents:
    print("\nFirst document:")
    print("Content:")
    print(documents[0].page_content[:500])

    print("\nMetadata:")
    print(documents[0].metadata)