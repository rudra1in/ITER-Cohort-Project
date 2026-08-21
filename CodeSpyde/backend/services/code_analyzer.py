import ast


def analyze_python_code(
    code: str
) -> dict:
    """
    Perform safe Python syntax analysis.

    This function DOES NOT execute the student's code.
    """

    if not code.strip():

        return {
            "valid": True,
            "issues": []
        }

    try:

        ast.parse(code)

        return {
            "valid": True,
            "issues": []
        }

    except SyntaxError as error:

        line = error.lineno or 1
        column = error.offset or 1

        return {
            "valid": False,
            "issues": [
                {
                    "line": line,
                    "column": column,
                    "end_line": line,
                    "end_column": column + 1,
                    "severity": "error",
                    "type": "syntax",
                    "message": error.msg
                }
            ]
        }


def analyze_code(
    code: str,
    language: str
) -> dict:

    normalized_language = (
        language.strip().lower()
    )

    if normalized_language == "python":

        return analyze_python_code(
            code
        )

    return {
        "valid": True,
        "issues": [],
        "message": (
            f"Static analysis for "
            f"{language} is not available yet."
        )
    }