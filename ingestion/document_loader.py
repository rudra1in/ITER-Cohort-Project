from pathlib import Path
import json


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [{
        "text": json.dumps(data, indent=2),
        "metadata": {
            "source": file_path.name,
            "file_type": "json"
        }
    }]


def load_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return [{
        "text": text,
        "metadata": {
            "source": file_path.name,
            "file_type": "txt"
        }
    }]


def load_documents(data_directory):

    data_directory = Path(data_directory)
    documents = []

    # Load JSON files
    for file_path in data_directory.rglob("*.json"):
        documents.extend(load_json(file_path))

    # Load TXT files
    for file_path in data_directory.rglob("*.txt"):
        documents.extend(load_txt(file_path))

    return documents


if __name__ == "__main__":

    data_path = Path(__file__).parent.parent / "data" / "txt"

    documents = load_documents(data_path)

    print(f"Total documents loaded: {len(documents)}")

    for i, document in enumerate(documents, start=1):

        print("\n" + "=" * 60)
        print(f"Document {i}")

        print("Metadata:")
        print(document["metadata"])

        print("\nText preview:")
        print(document["text"][:500])