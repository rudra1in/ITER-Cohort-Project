from fastapi import APIRouter, HTTPException


router = APIRouter(
    prefix="/api/problems",
    tags=["Problems"]
)


PROBLEMS = [
    {
        "id": "two-sum",
        "title": "Two Sum",
        "description": (
            "Given an array of integers nums "
            "and an integer target, return indices "
            "of the two numbers such that they add "
            "up to target."
        ),
        "topic": "Arrays",
        "difficulty": "Easy",
        "pattern": "Hash Map",
        "constraints": (
            "Each input has exactly one solution."
        ),
        "examples": [
            {
                "input": "[2,7,11,15], target=9",
                "output": "[0,1]"
            }
        ],
        "test_cases": [
            {
                "input": [
                    [2, 7, 11, 15],
                    9
                ],
                "expected_output": [0, 1]
            },
            {
                "input": [
                    [3, 2, 4],
                    6
                ],
                "expected_output": [1, 2]
            }
        ]
    },

    {
        "id": "reverse-array",
        "title": "Reverse Array",
        "description": (
            "Given an array, return the array "
            "with its elements reversed."
        ),
        "topic": "Arrays",
        "difficulty": "Easy",
        "pattern": "Two Pointers",
        "constraints": "",
        "examples": [
            {
                "input": "[1,2,3,4]",
                "output": "[4,3,2,1]"
            }
        ],
        "test_cases": [
            {
                "input": [[1, 2, 3, 4]],
                "expected_output": [4, 3, 2, 1]
            }
        ]
    }
]


@router.get("")
async def get_problems():

    return {
        "count": len(PROBLEMS),
        "problems": PROBLEMS
    }


@router.get("/{problem_id}")
async def get_problem(
    problem_id: str
):

    for problem in PROBLEMS:

        if problem["id"] == problem_id:
            return problem

    raise HTTPException(
        status_code=404,
        detail="Problem not found."
    )