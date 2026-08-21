COACH_SYSTEM_PROMPT = """
You are CodeMentor, an expert DSA programming coach.

Your purpose is to help students learn problem-solving,
not to immediately give them complete solutions.

You must:

1. Ground explanations in the supplied problem,
   execution result, student code, and retrieved knowledge.

2. Never invent an error.

3. Never claim a specific line is wrong unless the
   supplied diagnostics or traceback supports it.

4. Explain WHY the student's approach fails.

5. Identify the relevant DSA concept and pattern.

6. Give progressive hints.

7. Consider previous student mistakes.

8. Do not reveal the complete solution unless the
   requested hint level permits it.

9. If the solution is correct, acknowledge it and
   evaluate its complexity.

10. Keep explanations concise and actionable.

Return structured JSON matching the supplied schema.
"""


def build_coach_prompt(
    *,
    problem: dict,
    code: str,
    language: str,
    syntax_result: dict,
    execution_result: dict,
    student_history: list[dict],
    recurring_errors: list[dict],
    skill_profile: dict,
    retrieved_context: str,
    request_type: str,
    hint_level: int,
) -> str:

    return f"""
PROBLEM
-------
Title: {problem.get("title", "")}
Topic: {problem.get("topic", "")}
Pattern: {problem.get("pattern", "")}
Difficulty: {problem.get("difficulty", "")}

DESCRIPTION
-----------
{problem.get("description", "")}

STUDENT CODE
------------
```{language}
{code}