import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

MODEL_NAME = "gemini-3.6-flash"

class MockLLM:

    def invoke(self, prompt):

        prompt_text = str(prompt).lower()

        if "hint agent" in prompt_text:
            answer = """
            Here is a hint for the problem:

            Think about what information you need to remember while
            scanning through the array.

            Ask yourself whether you can avoid checking every possible pair.

            Try to identify a data structure that can help you quickly
            check whether the value you need has already appeared.
            """

        elif "code agent" in prompt_text:
            answer = """
            Let's analyze your code.

            First, trace the code with a small example and identify the
            first point where the actual behavior differs from what you
            expect.

            Also check the time and space complexity of your approach.
            """
        elif "interview agent" in prompt_text:
            answer = """
            Interview Question:

            Explain the difference between an ArrayList and a LinkedList
            in Java.

            Answer the question as if you were in a technical interview.
            """

        elif "mcq agent" in prompt_text:
            answer = """
            Which data structure provides average O(1) lookup time?

            A. ArrayList
            B. LinkedList
            C. HashMap
            D. Stack

            Choose one option and explain your reasoning.
            """

        elif "roadmap agent" in prompt_text:
            answer = """
            A good DSA learning sequence is:

            1. Arrays
            2. Strings
            3. Hashing
            4. Two Pointers
            5. Sliding Window
            6. Linked Lists
            7. Stack and Queue
            8. Trees
            9. Graphs
            10. Dynamic Programming

            Focus on patterns rather than memorizing individual solutions.
            """

        else:
            answer = """
            This is a mock AI response.

            Start by identifying:
            1. What the problem is asking.
            2. What information you need to maintain.
            3. Which data structure or algorithm can make the operation efficient.
            """

        return MockResponse(answer)

class MockResponse:

    def __init__(self, content):
        self.content = content

def create_llm() -> ChatGoogleGenerativeAI:
    """
    Create the Gemini LLM used by the DSA Coach.

    USE_MOCK_LLM=true  -> Local mock response, no Gemini API call.
    USE_MOCK_LLM=false -> Real Gemini.
    """

    use_mock = os.getenv(
        "USE_MOCK_LLM",
        "false"
    ).lower() == "true"

    # --------------------------------------------------------
    # MOCK MODE
    # --------------------------------------------------------

    if use_mock:
        print("⚠️ MOCK LLM ENABLED — Gemini will NOT be called.")
        return MockLLM()

    # --------------------------------------------------------
    # REAL GEMINI MODE
    # --------------------------------------------------------

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not configured in the .env file."
        )

    print("🤖 REAL GEMINI LLM ENABLED")

    return ChatGoogleGenerativeAI(
        model=MODEL_NAME,
        api_key=api_key,
        temperature=0.2,
    )