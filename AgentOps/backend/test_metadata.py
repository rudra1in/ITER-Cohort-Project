from app.rag.loader import load_dsa_documents
from app.rag.metadata import merge_duplicate_problems


documents = load_dsa_documents()

processed_documents = merge_duplicate_problems(documents)

print("\n========== METADATA TEST ==========")

print(f"Original documents: {len(documents)}")
print(f"Unique problems: {len(processed_documents)}")

print("\n========== FIRST PROBLEM ==========")

doc = processed_documents[0]

print("Title:", doc.metadata["title"])
print("Problem ID:", doc.metadata["problem_id"])
print("Difficulty:", doc.metadata["difficulty"])
print("Topic:", doc.metadata["topic"])
print("Topics:", doc.metadata["topics"])
print("Pattern:", doc.metadata["pattern"])