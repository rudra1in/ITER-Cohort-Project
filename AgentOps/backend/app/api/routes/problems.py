from pathlib import Path

from fastapi import APIRouter, HTTPException


router = APIRouter(
    prefix="/api/problems",
    tags=["Problems"],
)


# backend/data/dsa
DATA_DIR = Path(__file__).resolve().parents[3] / "data" / "dsa"


def parse_problem_file(file_path: Path, topic: str):
    content = file_path.read_text(
        encoding="utf-8"
    )

    problem = {
        "id": file_path.stem,
        "topic": topic,
        "title": "",
        "problem": "",
        "pattern": "",
        "brute_force": "",
        "optimized_approach": "",
        "hint_1": "",
        "hint_2": "",
        "common_mistakes": "",
        "complexity": "",
    }

    lines = content.splitlines()

    current_section = None
    section_content = []

    for line in lines:

        # Main title
        if line.startswith("# ") and not problem["title"]:
            problem["title"] = line[2:].strip()
            continue

        # Section heading
        if line.startswith("## "):

            if current_section:
                problem[current_section] = "\n".join(
                    section_content
                ).strip()

            section_content = []

            heading = line[3:].strip().lower()

            section_map = {
                "problem": "problem",
                "pattern": "pattern",
                "brute force approach": "brute_force",
                "optimized approach": "optimized_approach",
                "hint 1": "hint_1",
                "hint 2": "hint_2",
                "common mistakes": "common_mistakes",
                "complexity": "complexity",
            }

            current_section = section_map.get(
                heading
            )

            continue

        if current_section:
            section_content.append(line)

    # Save final section
    if current_section:
        problem[current_section] = "\n".join(
            section_content
        ).strip()

    return problem


@router.get("/")
def get_problems():
    problems = []

    if not DATA_DIR.exists():
        raise HTTPException(
            status_code=500,
            detail="DSA data directory not found.",
        )

    for topic_dir in DATA_DIR.iterdir():

        if not topic_dir.is_dir():
            continue

        for file_path in topic_dir.glob("*.md"):

            try:
                problem = parse_problem_file(
                    file_path,
                    topic_dir.name,
                )

                problems.append(problem)

            except Exception as error:
                print(
                    f"Failed to read {file_path}: {error}"
                )

    return {
        "count": len(problems),
        "problems": problems,
    }