import json
from agents.graph import agent

MAX_POINTS = {"Correctness": 4, "Efficiency": 3, "Readability": 2, "Approach": 1}

with open("data/txt/dsa_questions.json", "r") as f:
    problems = json.load(f)

print("\n========== DSA PROBLEM BANK ==========\n")
for i, p in enumerate(problems, 1):
    explanation = p.get("explanation", "A classic DSA problem to practice.")
    print(f"{i}. {p['problem']} — {explanation}")

choice = int(input("\n👉 Which problem would you like to solve? Enter the number: ")) - 1
selected = problems[choice]

print("\n======================================")
print(f"🎯 Selected Problem: {selected['problem']}")
print("======================================\n")

approach = input("✍️ First, tell me your approach in your own words: ")
print("\n💻 Great! Now paste your code below.\n")
code = input()

print("\n⏳ DSA Coach is analyzing your solution... hang tight!\n")

test_input = {
    "problem": selected["problem"],
    "approach": approach,
    "code": code,
    "retrieved_knowledge": [],
    "analysis": "",
    "complexity": "",
    "evaluation": "",
    "feedback": "",
    "hint": "",
    "scorecard": {},
    "score_history": [],
    "score": 0,
    "avg_score": 0,
    "intro": "",
    "encouragement": ""
}

result = agent.invoke(test_input)

print("\n======================================")
print("          📚 DSA COACH RESULT")
print("======================================\n")

print(result.get("intro", ""))
print(result.get("analysis", ""))
print(result.get("complexity", ""))
print(result.get("evaluation", ""))
print(result.get("hint", ""))
print(result.get("feedback", ""))

print("\n========== SCORECARD ==========")
sc = result.get("scorecard", {})
for cat in ["Correctness", "Efficiency", "Readability", "Approach"]:
    print(f"{cat}: {sc.get(cat, 0)}/{MAX_POINTS[cat]}")
print(f"Total: {sc.get('Total', 0)}/10")

print("\n========== PROGRESS TRACKER ==========")
print(f"Latest score: {result['score']}/10")
print(f"Average score across {len(result['score_history'])} problems: {result['avg_score']:.2f}/10")

print("\n📊 Progress Graph:")
for i, s in enumerate(result["score_history"], 1):
    bar = "█" * s + "-" * (10 - s)
    print(f"Problem {i}: {bar} {s}/10")

print("\n🌟 Daily Motivation:")
print(result.get("encouragement", "Keep pushing forward — every problem solved sharpens your skills! 🚀"))