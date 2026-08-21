
import json
import os
import re

from agents.memory import load_progress, save_progress


OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")


def _ollama_chat(prompt):
    from ollama import chat

    response = chat(
        model=OLLAMA_MODEL,
        messages=[{"role": "user", "content": prompt}],
        options={"num_predict": 1200},
    )
    return response["message"]["content"]


def _extract_json(text):
    if not text:
        return {}

    text = text.strip()

    try:
        return json.loads(text)
    except Exception:
        pass

    # Remove ```json fences if the model adds them.
    cleaned = re.sub(r"```(?:json)?", "", text, flags=re.I).replace("```", "")

    try:
        return json.loads(cleaned.strip())
    except Exception:
        pass

    match = re.search(r"\{.*\}", cleaned, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except Exception:
            pass

    return {}


def _clamp_number(value, low, high):
    try:
        return max(low, min(high, int(float(value))))
    except Exception:
        return low


def retrieve_knowledge(state):
    """
    RAG is optional. The evaluator continues even when PostgreSQL/pgvector
    is not running, which prevents the UI from crashing.
    """
    try:
        from retrieval.retrieve import retrieve_chunks

        chunks = retrieve_chunks(state["problem"], top_k=4)
        knowledge = [item["text"] for item in chunks]
    except Exception as exc:
        print(f"[retrieve_knowledge] skipped: {exc}")
        knowledge = []

    return {
        **state,
        "retrieved_knowledge": knowledge,
    }


def coach_submission(state):
    progress = load_progress()

    knowledge = "\n\n".join(
        state.get("retrieved_knowledge", [])
    )

    prompt = f"""
You are CodeCurry, an intelligent DSA coach for students.

Evaluate the student's submission honestly and constructively.

You MUST return ONLY valid JSON. Do not use markdown.
Do not write X/4, X/3, etc. Put actual integer numbers in scorecard.

Scoring:
Correctness: 0-4
Efficiency: 0-3
Readability: 0-2
Approach: 0-1
Total must equal the sum and therefore be 0-10.

Use this exact JSON structure:
{{
  "intro": "friendly one or two sentence summary",
  "analysis": "what the student did and whether the logic is sound",
  "complexity": "time and space complexity with reasoning",
  "evaluation": "edge cases and correctness assessment",
  "hint": "one useful hint without unnecessarily giving the full solution",
  "feedback": "2-4 concrete improvements",
  "encouragement": "short motivating message",
  "scorecard": {{
    "Correctness": 0,
    "Efficiency": 0,
    "Readability": 0,
    "Approach": 0
  }}
}}

Problem:
{state.get("problem", "")}

Relevant DSA knowledge:
{knowledge}

Student approach:
{state.get("approach", "")}

Language:
{state.get("language", "Unknown")}

Student code:
{state.get("code", "")}
"""

    try:
        raw = _ollama_chat(prompt)
        data = _extract_json(raw)
    except Exception as exc:
        print(f"[coach_submission] Ollama unavailable: {exc}")
        data = {}

    sc = data.get("scorecard", {})

    correctness = _clamp_number(sc.get("Correctness"), 0, 4)
    efficiency = _clamp_number(sc.get("Efficiency"), 0, 3)
    readability = _clamp_number(sc.get("Readability"), 0, 2)
    approach_score = _clamp_number(sc.get("Approach"), 0, 1)

    total = correctness + efficiency + readability + approach_score

    # Never show a fake 0/10 merely because JSON parsing failed.
    # When AI is unavailable, use a clearly marked fallback evaluation.
    if not data:
        code = state.get("code", "")
        approach = state.get("approach", "")

        has_code = bool(code.strip())
        has_approach = bool(approach.strip())

        readability = 1 if has_code else 0
        approach_score = 1 if has_approach else 0
        correctness = 1 if has_code else 0
        efficiency = 1 if has_code else 0
        total = correctness + efficiency + readability + approach_score

        data = {
            "intro": "🧑‍🏫 Your submission is ready for review.",
            "analysis": (
                "The AI evaluator could not be reached, so this is a "
                "basic local submission check rather than a correctness verdict."
            ),
            "complexity": (
                "Run the configured CodeCurry evaluator to get detailed "
                "time and space complexity analysis."
            ),
            "evaluation": (
                "Your code and approach were detected. A full correctness "
                "check requires the Ollama coach to be running."
            ),
            "hint": "Check edge cases and state the expected complexity.",
            "feedback": (
                "Start Ollama and make sure the selected model is available "
                "for the full AI evaluation."
            ),
            "encouragement": "🚀 Your practice session is still valuable — keep going!",
        }

    history = progress.get("score_history", [])
    history = [
        max(0, min(10, int(float(x))))
        for x in history
        if str(x).replace(".", "", 1).isdigit()
    ]
    history.append(total)

    avg_score = sum(history) / len(history)

    save_progress(
        history,
        avg_score,
        progress.get("solved_ids", []),
    )

    return {
        **state,
        "intro": data.get("intro", "🎉 Nice work — let's review it."),
        "analysis": data.get(
            "analysis",
            "Your submission was reviewed against the problem requirements.",
        ),
        "complexity": data.get(
            "complexity",
            "Complexity analysis is unavailable.",
        ),
        "evaluation": data.get(
            "evaluation",
            "Review edge cases carefully.",
        ),
        "hint": data.get(
            "hint",
            "Look for a data structure that reduces repeated work.",
        ),
        "feedback": data.get(
            "feedback",
            "Make one measurable improvement in your next attempt.",
        ),
        "encouragement": data.get(
            "encouragement",
            f"🚀 Your current average is {avg_score:.1f}/10.",
        ),
        "scorecard": {
            "Correctness": correctness,
            "Efficiency": efficiency,
            "Readability": readability,
            "Approach": approach_score,
            "Total": total,
        },
        "score": total,
        "score_history": history,
        "avg_score": avg_score,
        "done": True,
    }


def progress_node(state):
    return {**state}


def motivation_node(state):
    avg = state.get("avg_score", 0)
    return {
        **state,
        "encouragement": state.get(
            "encouragement",
            f"🚀 Keep going! Your average score is {avg:.1f}/10.",
        ),
    }
