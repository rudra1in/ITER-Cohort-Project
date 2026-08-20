from app.rag.retriever import similarity_search


def main():

    query = (
        "How do I find the maximum element in an array?"
    )

    print("\n================================")
    print("QUERY")
    print("================================")

    print(query)

    print("\nSearching knowledge base...\n")

    documents = similarity_search(
        query=query,
        top_k=5,
    )

    print(
        f"Retrieved {len(documents)} chunks.\n"
    )

    for index, document in enumerate(
        documents,
        start=1,
    ):

        print("================================")
        print(f"RESULT {index}")
        print("================================")

        print(
            f"Problem ID: "
            f"{document.metadata.get('problem_id')}"
        )

        print(
            f"Title: "
            f"{document.metadata.get('title')}"
        )

        print(
            f"Topic: "
            f"{document.metadata.get('topic')}"
        )

        print(
            f"Difficulty: "
            f"{document.metadata.get('difficulty')}"
        )

        print(
            f"Pattern: "
            f"{document.metadata.get('pattern')}"
        )

        print(
            f"Section: "
            f"{document.metadata.get('section')}"
        )

        print(
            f"Distance: "
            f"{document.metadata.get('distance')}"
        )

        print("\nContent:")

        print(
            document.page_content[:1000]
        )

        print()


if __name__ == "__main__":
    main()