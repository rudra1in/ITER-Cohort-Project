from pathlib import Path
import json


def chunk_json_document(document):
    """
    Convert the JSON document containing the 20 DSA questions
    into one chunk per question.
    """

    data = json.loads(document["text"])

    chunks = []

    for question in data:

        # Convert the question into searchable text
        text = f"""
Problem: {question.get("problem", "")}

Difficulty: {question.get("difficulty", "")}

Topic: {question.get("topic", "")}

Description:
{question.get("description", "")}

Examples:
{question.get("examples", [])}

Expected Concepts:
{question.get("expected_concepts", [])}
""".strip()

        chunks.append({
            "text": text,
            "metadata": {
                "source": document["metadata"]["source"],
                "file_type": "json",
                "problem_id": question.get("id"),
                "problem": question.get("problem"),
                "difficulty": question.get("difficulty"),
                "topic": question.get("topic")
            }
        })

    return chunks


def chunk_document(document):

    if document["metadata"]["file_type"] == "json":
        return chunk_json_document(document)

    # For TXT files
    text = document["text"]

    return [{
        "text": text,
        "metadata": document["metadata"]
    }]


def create_chunks(documents):

    all_chunks = []

    for document in documents:

        chunks = chunk_document(document)

        all_chunks.extend(chunks)

    return all_chunks


if __name__ == "__main__":

    from document_loader import load_documents

    data_path = Path(__file__).parent.parent / "data" / "txt"

    documents = load_documents(data_path)

    print(f"Documents loaded: {len(documents)}")

    chunks = create_chunks(documents)

    print(f"Total chunks created: {len(chunks)}")

    for i, chunk in enumerate(chunks, start=1):

        print("\n" + "=" * 60)
        print(f"CHUNK {i}")

        print("Metadata:")
        print(chunk["metadata"])

        print("\nText:")
        print(chunk["text"][:500])