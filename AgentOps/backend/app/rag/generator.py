import os
from typing import List

from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage, SystemMessage

from app.rag.llm import create_llm


# ============================================================
# ENVIRONMENT
# ============================================================

load_dotenv()

USE_MOCK_LLM = os.getenv(
    "USE_MOCK_LLM",
    "true",
).lower() == "true"


# ============================================================
# SYSTEM PROMPT
# ============================================================

SYSTEM_PROMPT = """
You are DSA Coach, an AI tutor specialized in
Data Structures and Algorithms.

Your job is to help students understand DSA concepts
and solve coding problems, analyze code, and prepare for
technical interviews.

IMPORTANT:

The retrieved knowledge is supporting reference material.
It is NOT a limitation on what you can explain.

If the retrieved knowledge is incomplete, irrelevant,
or does not contain the exact topic asked by the student,
use your general DSA knowledge to answer the question.

NEVER tell the student that the knowledge base,
retrieved context, documents, RAG system, or internal
knowledge was insufficient.

NEVER mention:

- knowledge base
- retrieved context
- retrieval
- RAG
- documents
- agents
- prompts
- Gemini
- internal systems

The student should only see the final educational answer.

Rules:

1. Answer the student's actual question directly.
2. Explain concepts at a beginner/fresher placement level.
3. Prefer clear step-by-step explanations.
4. When explaining an algorithm, explain:
   - the idea
   - the steps
   - why it works
   - time complexity
   - space complexity
5. If code is requested, provide code in the programming
   language specified by the student.
6. Keep explanations practical and interview-oriented.
7. If the retrieved material is relevant, use it to
   improve accuracy and consistency.

8. If the retrieved material is irrelevant or incomplete,
   do NOT mention this to the student. Answer using your
   general DSA knowledge.
9. Never respond to an explanation request by asking
    the student a question.

10. If the user says "explain X", directly explain X.

11. Do not turn an explanation into a Socratic question
    unless the user explicitly asks for hints or interactive
    questioning.

12. If the retrieved context contains questions, exercises,
    or prompts, treat them as reference material and do not
    repeat them as questions to the student.

13. Give a complete explanation rather than asking the
    student to figure out the answer themselves.
14. Format your response using clean standard Markdown.

15. Use Markdown syntax normally:
    - **bold**
    - *italic*
    - `inline code`
    - fenced code blocks
    - Markdown headings
    - Markdown bullet lists
    - Markdown tables

16. Never escape Markdown characters unnecessarily.
    For example, write **O(N)**, not \*\*O(N)\*.

17. Never duplicate or transform Markdown formatting characters.
    For example, never produce:
    **O(N)*****O*****(*****N*****)

18. For algorithmic complexity, write complexity normally,
    such as **O(N)**, **O(log N)**, or **O(N log N)**.

19. Do not use LaTeX for simple Big-O notation unless necessary.
    Prefer **O(N)** instead of $O(N)$.

20. If you use a Markdown table, use standard Markdown table syntax
    with one | separator between each column.

21. Do not begin an answer with phrases such as:

    "The retrieved knowledge..."
    "The knowledge base..."
    "The provided context..."
    "According to the retrieved documents..."
    "I could not find..."
    "The context does not contain..."

22. Never expose limitations of the retrieval system to
    the student.
"""


# ============================================================
# BUILD CONTEXT
# ============================================================

def build_context(
    documents: List[Document],
) -> str:

    if not documents:
        return "No additional reference material was retrieved."

    context_parts = []

    for index, document in enumerate(
        documents,
        start=1,
    ):

        metadata = document.metadata

        context_parts.append(
            f"""
--- CONTEXT {index} ---

Problem ID:
{metadata.get("problem_id", "unknown")}

Title:
{metadata.get("title", "unknown")}

Topic:
{metadata.get("topic", "unknown")}

Difficulty:
{metadata.get("difficulty", "unknown")}

Pattern:
{metadata.get("pattern", "unknown")}

Section:
{metadata.get("section", "unknown")}

Content:
{document.page_content}
"""
        )

    return "\n".join(context_parts)



# ============================================================
# GENERATE ANSWER
# ============================================================

def generate_answer(
    query: str,
    documents: List[Document],
    language: str = "java",
) -> str:


    print("\n========== RETRIEVED CONTEXT ==========")

    context = build_context(documents)

    print(context)

    print("========== END RETRIEVED CONTEXT ==========\n")

    # --------------------------------------------------------
    # USER PROMPT
    # --------------------------------------------------------

    user_prompt = f"""
Answer the student's DSA question.

Student Question:
{query}

Programming Language:
{language}

Retrieved Knowledge:
{context}

IMPORTANT:

The reference material is only supporting information.

If it contains the answer or useful information,
use it.

If it does not contain the answer, use your general
knowledge of Data Structures and Algorithms.

Do NOT tell the student that the reference material
was missing, incomplete, irrelevant, or insufficient.

Do NOT mention:

- retrieval
- RAG
- knowledge base
- documents
- reference material
- agents
- prompts
- Gemini
- internal systems

Simply answer the student's question as a DSA tutor

Answer the question directly.

For explanation requests:
- Start with the definition.
- Explain the concept clearly.
- Give an intuitive explanation.
- Give an example when useful.
- Explain important properties.
- Explain time and space complexity when relevant.

For algorithm questions:
- Explain the idea.
- Explain the steps.
- Explain why it works.
- Give complexity.
- Give Java code when appropriate.

For comparison questions:
- Explain both concepts.
- Clearly compare them.
- Use a table when useful.

For follow-up questions:
- Use the conversation provided in the query.
- Resolve references such as "it", "its", "this",
  "that", and "the above approach".

If the user asks for code:
- Use the requested programming language.
- Provide complete working code.
- Explain the important parts briefly.

OUTPUT FORMAT:

Return clean standard Markdown.

Use:
- **bold**
- `inline code`
- fenced code blocks
- headings
- bullet lists
- Markdown tables when useful

For Big-O notation, write:

**O(1)**
**O(N)**
**O(log N)**
**O(N log N)**

Do not escape Markdown characters.

Do not duplicate Markdown characters.
"""

    # --------------------------------------------------------
    # CREATE LLM
    # --------------------------------------------------------

    llm = create_llm()

    # --------------------------------------------------------
    # CALL GEMINI
    # --------------------------------------------------------

    response = llm.invoke(
        [
            SystemMessage(
                content=SYSTEM_PROMPT
            ),
            HumanMessage(
                content=user_prompt
            ),
        ]
    )

    # --------------------------------------------------------
    # RETURN ANSWER
    # --------------------------------------------------------

    return response.content