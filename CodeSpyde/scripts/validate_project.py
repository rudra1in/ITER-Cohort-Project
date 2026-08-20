#!/usr/bin/env python
"""
scripts/validate_project.py

Validates all subsystems of the AI DSA Coach:
- Subsystem imports and configuration
- PostgreSQL and pgvector database status
- Embeddings and search pipelines (vector, keyword, RRF)
- Reranker (Cross-Encoder)
- LangGraph agent nodes and state transitions
- Validation of 5 student code scenarios (Syntax Error, Runtime Error, Wrong Answer, Timeout, Accepted)
"""

import sys
import argparse
import traceback
import json
from pathlib import Path

# Add backend directory to path
BACKEND_DIR = Path(__file__).resolve().parent.parent / "backend"
sys.path.insert(0, str(BACKEND_DIR))

# Import core settings and DB helper
from config import DATABASE_URL, RERANKER_ENABLED, EMBEDDING_DIMENSION
from database import get_db_cursor, execute_sql


def run_checks(live: bool = False):
    print("==================================================")
    print(f"DSA COACH SYSTEM VALIDATION (LIVE MODE: {live})")
    print("==================================================")

    # --------------------------------------------------
    # 1. Imports and Configuration
    # --------------------------------------------------
    print("\n1. [IMPORTS & CONFIGURATION]")
    try:
        from routes.code import router as code_router
        from routes.problems import router as problems_router
        from routes.rag import router as rag_router
        from routes.coach import router as coach_router
        from agent.graph import dsa_coach_graph
        print("  [PASS] All API routes and graph imported successfully.")
    except Exception as e:
        print(f"  [FAIL] Import validation failed:\n{traceback.format_exc()}")
        return False

    # --------------------------------------------------
    # 2. Database Connection and Schema
    # --------------------------------------------------
    print("\n2. [DATABASE STATUS]")
    try:
        with get_db_cursor() as cursor:
            # Check connection
            cursor.execute("SELECT version();")
            version = cursor.fetchone()[0]
            print(f"  [PASS] Connected to: {version}")

            # Check pgvector extension
            cursor.execute("SELECT extname FROM pg_extension WHERE extname = 'vector';")
            vector_ext = cursor.fetchone()
            if vector_ext:
                print("  [PASS] pgvector extension is installed.")
            else:
                print("  [INFO] pgvector extension is NOT installed. Running CREATE EXTENSION...")
                cursor.execute("CREATE EXTENSION IF NOT EXISTS vector;")
                print("  [PASS] pgvector extension created successfully.")

            # Check tables
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
            tables = [r[0] for r in cursor.fetchall()]
            required_tables = ["dsa_documents", "dsa_chunks", "student_attempts", "token_usage"]
            for table in required_tables:
                if table in tables:
                    print(f"  [PASS] Table '{table}' exists.")
                else:
                    print(f"  [FAIL] Table '{table}' is MISSING!")
                    return False
    except Exception as e:
        print(f"  [FAIL] Database check failed:\n{traceback.format_exc()}")
        return False

    # --------------------------------------------------
    # 3. Seed Mock Knowledge Base
    # --------------------------------------------------
    print("\n3. [DATABASE SEEDING]")
    mock_doc_id = "00000000-0000-0000-0000-000000000001"
    mock_chunk_id = "00000000-0000-0000-0000-000000000002"
    try:
        with get_db_cursor() as cursor:
            # Ensure mock doc & chunk exist for RAG validation
            cursor.execute("DELETE FROM dsa_chunks WHERE id = %s;", (mock_chunk_id,))
            cursor.execute("DELETE FROM dsa_documents WHERE id = %s;", (mock_doc_id,))

            cursor.execute(
                """
                INSERT INTO dsa_documents (id, title, document_type, topic, subtopic, pattern, difficulty)
                VALUES (%s, 'Two Sum Solution Guide', 'solution', 'Arrays', 'Two Sum', 'Two Pointers', 'Easy');
                """,
                (mock_doc_id,)
            )

            # 768 dimension mock vector
            mock_vector = [0.1] * EMBEDDING_DIMENSION

            cursor.execute(
                """
                INSERT INTO dsa_chunks (id, document_id, chunk_index, chunk_type, title, content, topic, subtopic, pattern, difficulty, embedding)
                VALUES (%s, %s, 0, 'code', 'Two Sum HashMap', 'Use a hash map to store visited elements and indices. Time complexity O(N), space complexity O(N).', 'Arrays', 'Two Sum', 'Two Pointers', 'Easy', %s);
                """,
                (mock_chunk_id, mock_doc_id, mock_vector)
            )
            print("  [PASS] Mock knowledge base seed inserted successfully.")
    except Exception as e:
        print(f"  [FAIL] Database seeding failed:\n{traceback.format_exc()}")
        return False

    # --------------------------------------------------
    # 4. Embeddings, Retrieval, and Reranking
    # --------------------------------------------------
    print("\n4. [RETRIEVAL & RAG PIPELINE]")
    try:
        # Mock embeddings if not live
        if not live:
            import embeddings.gemini_embeddings as ge
            import retrieval.hybrid_search as hs
            mock_emb = lambda text: [0.1] * EMBEDDING_DIMENSION
            ge.create_embedding = mock_emb
            hs.create_embedding = mock_emb
            print("  [PASS] Mocked Gemini embeddings created successfully.")
        else:
            from embeddings.gemini_embeddings import create_embedding
            emb = create_embedding("two sum hash map")
            print(f"  [PASS] Live Gemini embedding generated successfully (dim={len(emb)}).")

        from retrieval.hybrid_search import hybrid_search
        results = hybrid_search(query="two sum hash map", topic="Arrays", limit=5)
        print(f"  [PASS] Hybrid search returned {len(results)} results.")

        # Test Reranker
        from retrieval.reranker import rerank
        if RERANKER_ENABLED:
            reranked = rerank(candidates=results, query="two sum hash map", limit=3)
            print(f"  [PASS] Reranker returned {len(reranked)} results.")
        else:
            print("  [PASS] Reranker is disabled in config.")
    except Exception as e:
        print(f"  [FAIL] Retrieval pipeline check failed:\n{traceback.format_exc()}")
        return False

    # --------------------------------------------------
    # 5. Gemini API and Scenario Routing
    # --------------------------------------------------
    print("\n5. [GEMINI & SCENARIO ROUTING]")
    
    # Standard Mock Coach Response
    mock_coach_ai_response = {
        "status": "Incorrect",
        "error_type": "SyntaxError",
        "error_line": 3,
        "explanation": "Missing colon after def statement.",
        "hint": "Check line 3 and add a colon at the end of the function declaration."
    }

    if not live:
        # Mock Gemini responses
        import services.ai_coach as ai_coach
        from models.schemas import CoachAIResponse
        
        class MockUsage:
            def model_dump(self):
                return {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15}

        def mock_generate_coach_response(prompt, model_name):
            data = mock_coach_ai_response.copy()
            if "ACCEPTED" in prompt:
                data["status"] = "Correct"
                data["error_type"] = None
                data["error_line"] = None
                data["explanation"] = "All test cases passed."
                data["hint"] = "Great work! Try optimizing to O(1) space if possible."
            elif "ZeroDivisionError" in prompt:
                data["status"] = "Incorrect"
                data["error_type"] = "ZeroDivisionError"
                data["error_line"] = 4
                data["explanation"] = "Division by zero."
                data["hint"] = "Ensure the denominator is not zero."
            elif "Wrong Answer" in prompt or "execution" in prompt:
                data["status"] = "Incorrect"
                data["error_type"] = "AssertionError"
                data["error_line"] = None
                data["explanation"] = "Fails test case: [3,3], target=6. Output is [0,0]."
                data["hint"] = "Make sure you don't reuse the same element index."
            elif "Timeout" in prompt or "Limit Exceeded" in prompt:
                data["status"] = "Incorrect"
                data["error_type"] = "Timeout"
                data["error_line"] = None
                data["explanation"] = "Code execution timed out."
                data["hint"] = "Avoid infinite loops or optimize nested iterations."

            return CoachAIResponse.model_validate(data), {
                "prompt_tokens": 150,
                "completion_tokens": 100,
                "total_tokens": 250
            }, 120

        ai_coach.generate_coach_response = mock_generate_coach_response
        print("  [PASS] Mocked Gemini Coach API successfully.")
    else:
        # Live run will check key
        from services.ai_coach import client
        print("  [PASS] Live Gemini client initialized.")

    # --------------------------------------------------
    # 6. LangGraph End-to-End Scenarios
    # --------------------------------------------------
    print("\n6. [LANGGRAPH SCENARIOS]")
    from agent.graph import dsa_coach_graph

    problems_db = {
        "two-sum": {
            "id": "two-sum",
            "title": "Two Sum",
            "topic": "Arrays",
            "pattern": "Two Pointers",
            "difficulty": "Easy",
            "description": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.",
            "test_cases": [
                {"input": [[2,7,11,15], 9], "expected_output": [0,1]},
                {"input": [[3,2,4], 6], "expected_output": [1,2]}
            ]
        }
    }

    # NOTE: Trace node names come from _add_trace() calls inside each node
    # function in backend/agent/nodes.py. These differ from the graph node
    # registration names in graph.py:
    #   graph name  -> trace name
    #   "memory"    -> "student_memory"
    #   "analyze"   -> "code_analysis"
    #   "execute"   -> "code_execution"
    # All others match.

    scenarios = [
        {
            "name": "Syntax Error",
            "code": "def solution(nums, target)\n    return [0, 1]",
            "expected_nodes": ["load_problem", "student_memory", "code_analysis", "model_router", "coach"]
        },
        {
            "name": "Runtime Error",
            "code": "def solution(nums, target):\n    return nums[10]",
            "expected_nodes": ["load_problem", "student_memory", "code_analysis", "code_execution", "build_query", "retrieve", "rerank", "model_router", "coach"]
        },
        {
            "name": "Wrong Answer",
            "code": "def solution(nums, target):\n    return [0, 0]",
            "expected_nodes": ["load_problem", "student_memory", "code_analysis", "code_execution", "build_query", "retrieve", "rerank", "model_router", "coach"]
        },
        {
            "name": "Timeout",
            "code": "def solution(nums, target):\n    while True:\n        pass",
            "expected_nodes": ["load_problem", "student_memory", "code_analysis", "code_execution", "model_router", "coach"]
        },
        {
            "name": "Accepted Solution",
            "code": "def solution(nums, target):\n    lookup = {} \n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in lookup:\n            return [lookup[diff], i]\n        lookup[num] = i\n    return []",
            "expected_nodes": ["load_problem", "student_memory", "code_analysis", "code_execution", "success"]
        }
    ]

    all_passed = True
    for scenario in scenarios:
        print(f"\nScenario: {scenario['name']}")
        try:
            # Inputs to the Graph
            inputs = {
                "user_id": "student_1",
                "problem_id": "two-sum",
                "code": scenario["code"],
                "language": "python",
                "request_type": "debug",
                "hint_level": 1,
            }

            # Run graph
            state = dsa_coach_graph.invoke(inputs)
            
            # Trace visited nodes
            visited_nodes = [t["node"] for t in state.get("trace", [])]
            print(f"  Nodes visited: {' -> '.join(visited_nodes)}")
            
            # Check expectations
            missing_nodes = [node for node in scenario["expected_nodes"] if node not in visited_nodes]
            if not missing_nodes:
                print("  [PASS] Scenario routed correctly.")
            else:
                print(f"  [FAIL] Scenario missing expected nodes: {missing_nodes}")
                all_passed = False

            coach_res = state.get("coach_response", {})
            print(f"  Coach response status: {coach_res.get('status')}")
            if scenario["name"] == "Accepted Solution":
                if state.get("solved") is True:
                    print("  [PASS] Accepted status confirmed.")
                else:
                    print("  [FAIL] Expected solved to be True.")
                    all_passed = False
            else:
                if coach_res.get("status") == "Incorrect":
                    print("  [PASS] Incorrect status confirmed.")
                else:
                    print("  [FAIL] Expected incorrect coach response status.")
                    all_passed = False

        except Exception as e:
            print(f"  [FAIL] Scenario execution crashed:\n{traceback.format_exc()}")
            all_passed = False

    # --------------------------------------------------
    # 7. Clean up database seeds
    # --------------------------------------------------
    try:
        with get_db_cursor() as cursor:
            cursor.execute("DELETE FROM dsa_chunks WHERE id = %s;", (mock_chunk_id,))
            cursor.execute("DELETE FROM dsa_documents WHERE id = %s;", (mock_doc_id,))
    except Exception:
        pass

    print("\n==================================================")
    if all_passed:
        print("PROJECT STATUS: COMPLETE (ALL CHECKS PASSED)")
        print("==================================================")
        return True
    else:
        print("PROJECT STATUS: INCOMPLETE (SOME CHECKS FAILED)")
        print("==================================================")
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate DSA Coach Project components.")
    parser.add_argument("--live", action="store_true", help="Run with live Gemini and embedding endpoints.")
    args = parser.parse_args()

    success = run_checks(live=args.live)
    if not success:
        sys.exit(1)
