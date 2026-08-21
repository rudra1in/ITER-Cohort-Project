from app.rag.service import ask_dsa_coach


queries = [
    "What is the time complexity of binary search?",
    "What is a linked list?",
    "How do I reverse a linked list?",
    "How do I find the maximum element in an array?",
]

for query in queries:

    print()
    print("================================")
    print("QUERY:")
    print(query)
    print("================================")

    result = ask_dsa_coach(query)

    print()
    print("ANSWER:")
    print(result["answer"])

    print()
    print("SOURCES:")

    for source in result["sources"]:
        print(
            source["problem_id"],
            "|",
            source["title"],
            "|",
            source["section"],
            "| distance=",
            source["distance"],
        )