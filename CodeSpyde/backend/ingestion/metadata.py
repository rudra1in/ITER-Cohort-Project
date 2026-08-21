KNOWN_TOPICS = {
    "arrays",
    "strings",
    "linked lists",
    "trees",
    "binary trees",
    "binary search trees",
    "graphs",
    "dynamic programming",
    "greedy",
    "backtracking",
    "recursion",
    "sorting",
    "searching",
    "hashing",
    "heaps",
    "priority queues",
    "stacks",
    "queues",
    "tries",
    "bit manipulation",
    "math"
}


KNOWN_PATTERNS = {
    "two pointers",
    "sliding window",
    "binary search",
    "prefix sum",
    "fast and slow pointers",
    "monotonic stack",
    "merge intervals",
    "top k elements",
    "backtracking",
    "divide and conquer",
    "breadth first search",
    "depth first search",
    "dynamic programming",
    "greedy",
    "union find"
}


KNOWN_DIFFICULTIES = {
    "easy",
    "medium",
    "hard"
}


def normalize_value(
    value
) -> str | None:

    if value is None:
        return None

    value = str(value).strip()

    return value or None


def infer_from_text(
    document: dict
) -> dict:

    text_parts = []

    for key in [
        "title",
        "content",
        "problem",
        "description",
        "approach",
        "intuition"
    ]:

        value = document.get(key)

        if value:

            text_parts.append(
                str(value)
            )

    text = " ".join(
        text_parts
    ).lower()

    result = {}

    # -----------------------------------------------------
    # Topic
    # -----------------------------------------------------

    topic = normalize_value(
        document.get("topic")
    )

    if not topic:

        for candidate in KNOWN_TOPICS:

            if candidate in text:

                topic = candidate.title()

                break

    result["topic"] = topic


    # -----------------------------------------------------
    # Pattern
    # -----------------------------------------------------

    pattern = normalize_value(
        document.get("pattern")
    )

    if not pattern:

        for candidate in KNOWN_PATTERNS:

            if candidate in text:

                pattern = candidate.title()

                break

    result["pattern"] = pattern


    # -----------------------------------------------------
    # Difficulty
    # -----------------------------------------------------

    difficulty = normalize_value(
        document.get("difficulty")
    )

    if difficulty:

        difficulty = difficulty.lower()

    if difficulty not in KNOWN_DIFFICULTIES:

        difficulty = None

    result["difficulty"] = difficulty


    # -----------------------------------------------------
    # Language
    # -----------------------------------------------------

    language = normalize_value(
        document.get("language")
    )

    result["language"] = language


    # -----------------------------------------------------
    # Complexity
    # -----------------------------------------------------

    result["time_complexity"] = normalize_value(
        document.get("time_complexity")
    )

    result["space_complexity"] = normalize_value(
        document.get("space_complexity")
    )


    return result


def extract_metadata(
    document: dict
) -> dict:

    inferred = infer_from_text(
        document
    )

    metadata = {
        **document,
        **inferred
    }

    return metadata