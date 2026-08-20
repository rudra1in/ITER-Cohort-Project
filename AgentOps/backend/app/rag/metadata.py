import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

from langchain_core.documents import Document


def extract_problem_id(document: Document) -> str:
    """
    Generate a stable problem ID from the Markdown filename.

    Example:
        3sum.md -> 3sum
        two_sum.md -> two_sum
    """

    filename = Path(document.metadata["filename"]).stem

    return filename.lower().strip()


def extract_title(document: Document) -> str:
    """
    Extract the first Markdown H1 heading.

    Example:
        # 15. 3Sum

    becomes:
        3Sum
    """

    content = document.page_content

    match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)

    if not match:
        return Path(document.metadata["filename"]).stem

    title = match.group(1).strip()

    # Remove problem number such as:
    # 15. 3Sum
    title = re.sub(r"^\d+\.\s*", "", title)

    return title


def extract_difficulty(document: Document) -> str:
    """
    Extract difficulty from the Markdown content.
    """

    content = document.page_content.lower()

    if "hard" in content:
        return "hard"

    if "medium" in content:
        return "medium"

    if "easy" in content:
        return "easy"

    return "unknown"


def extract_pattern(document: Document) -> str:
    """
    Extract the Pattern field from the Markdown document.

    Example:

        Pattern: **Linear Scan**

    becomes:

        Linear Scan
    """

    content = document.page_content

    match = re.search(
        r"^Pattern:\s*(.+)$",
        content,
        re.IGNORECASE | re.MULTILINE,
    )

    if not match:
        return "unknown"

    pattern = match.group(1).strip()

    # Remove Markdown bold markers
    pattern = pattern.replace("**", "")

    return pattern.strip()


def add_metadata(document: Document) -> Document:
    """
    Add structured metadata to a loaded document.
    """

    problem_id = extract_problem_id(document)
    title = extract_title(document)
    difficulty = extract_difficulty(document)
    pattern = extract_pattern(document)

    topic = document.metadata.get(
        "topic_folder",
        "unknown",
    )

    document.metadata.update(
        {
            "problem_id": problem_id,
            "title": title,
            "difficulty": difficulty,
            "topic": topic,
            "pattern": pattern,
        }
    )

    return document


def merge_duplicate_problems(
    documents: List[Document],
) -> List[Document]:
    """
    Merge documents representing the same problem.

    A problem may exist in multiple topic folders.
    Instead of indexing duplicates, merge their topic metadata.
    """

    problems: Dict[str, Document] = {}
    topics_by_problem = defaultdict(set)

    for document in documents:

        document = add_metadata(document)

        problem_id = document.metadata["problem_id"]
        topic = document.metadata["topic"]

        topics_by_problem[problem_id].add(topic)

        if problem_id not in problems:
            problems[problem_id] = document

    # Add all discovered topics to the surviving document
    for problem_id, document in problems.items():

        document.metadata["topics"] = sorted(
            topics_by_problem[problem_id]
        )

    return list(problems.values())