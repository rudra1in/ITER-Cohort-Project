# chunking.py
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
    CharacterTextSplitter,
    TokenTextSplitter
)

def chunk_text(text):
    # Technique 1: RecursiveCharacterTextSplitter
    recursive_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    recursive_chunks = recursive_splitter.split_text(text)

    # Technique 2: CharacterTextSplitter
    char_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=500,
        chunk_overlap=50
    )
    char_chunks = char_splitter.split_text(text)

    # Technique 3: TokenTextSplitter
    token_splitter = TokenTextSplitter(
        chunk_size=256,
        chunk_overlap=20
    )
    token_chunks = token_splitter.split_text(text)

    print("🔹 RecursiveCharacterTextSplitter produced:", len(recursive_chunks), "chunks")
    print("🔹 CharacterTextSplitter produced:", len(char_chunks), "chunks")
    print("🔹 TokenTextSplitter produced:", len(token_chunks), "chunks")

    # Return all three sets for evaluation
    return {
        "recursive": recursive_chunks,
        "character": char_chunks,
        "token": token_chunks
    }
