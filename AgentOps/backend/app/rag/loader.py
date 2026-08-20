from pathlib import Path
from typing import List

from langchain_core.documents import Document


# Location of the DSA knowledge base
DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "dsa"


def load_dsa_documents() -> List[Document]:
    """
    Recursively load all Markdown files from the DSA knowledge base.

    Each Markdown file becomes a LangChain Document.
    """

    documents = []

    if not DATA_DIR.exists():
        raise FileNotFoundError(
            f"DSA data directory not found: {DATA_DIR}"
        )

    markdown_files = list(DATA_DIR.rglob("*.md"))

    print(f"Found {len(markdown_files)} Markdown files.")

    for file_path in markdown_files:

        try:
            content = file_path.read_text(
                encoding="utf-8"
            )

            if not content.strip():
                print(f"Skipping empty file: {file_path}")
                continue

            document = Document(
                page_content=content,
                metadata={
                    "source": str(file_path),
                    "filename": file_path.name,
                    "topic_folder": file_path.parent.name,
                },
            )

            documents.append(document)

        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    print(f"Successfully loaded {len(documents)} documents.")

    return documents