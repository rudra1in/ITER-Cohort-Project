import requests
from typing import Dict, Any, List, Optional
from frontend.config import API_BASE_URL

class DSAClient:
    """Client for communicating with the AI DSA Coach FastAPI Backend."""
    
    def __init__(self, base_url: str = API_BASE_URL, timeout: float = 12.0):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def check_health(self) -> bool:
        """Check if backend service is available."""
        try:
            res = requests.get(f"{self.base_url}/health", timeout=3.0)
            return res.status_code == 200
        except Exception:
            return False

    def get_problems(self) -> Dict[str, Any]:
        """Fetch list of all DSA problems."""
        try:
            res = requests.get(f"{self.base_url}/api/problems", timeout=self.timeout)
            if res.status_code == 200:
                return res.json()
            return {"count": 0, "problems": [], "error": f"HTTP {res.status_code}: {res.text}"}
        except Exception as e:
            return {"count": 0, "problems": [], "error": f"Failed to connect to backend at {self.base_url}: {str(e)}"}

    def get_problem(self, problem_id: str) -> Optional[Dict[str, Any]]:
        """Fetch details for a specific problem by ID."""
        try:
            res = requests.get(f"{self.base_url}/api/problems/{problem_id}", timeout=self.timeout)
            if res.status_code == 200:
                return res.json()
            return None
        except Exception:
            return None

    def analyze_code(self, code: str, language: str = "python") -> Dict[str, Any]:
        """Analyze code statically via backend service."""
        try:
            res = requests.post(
                f"{self.base_url}/api/code/analyze",
                json={"code": code, "language": language},
                timeout=self.timeout
            )
            if res.status_code == 200:
                return res.json()
            return {"valid": False, "issues": [{"line": 1, "column": 1, "severity": "error", "type": "BackendError", "message": f"API Error: {res.status_code}"}]}
        except Exception as e:
            return {"valid": False, "issues": [{"line": 1, "column": 1, "severity": "error", "type": "ConnectionError", "message": f"Backend unreachable: {str(e)}"}]}

    def execute_code(self, code: str, language: str = "python", test_cases: List[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute code against test cases via backend execution engine."""
        payload = {
            "code": code,
            "language": language,
            "test_cases": test_cases or []
        }
        try:
            res = requests.post(
                f"{self.base_url}/api/code/execute",
                json=payload,
                timeout=self.timeout
            )
            if res.status_code == 200:
                return res.json()
            return {
                "status": "error",
                "stdout": "",
                "stderr": f"Backend Execution Error (HTTP {res.status_code}): {res.text}",
                "runtime_ms": 0,
                "test_results": []
            }
        except Exception as e:
            return {
                "status": "error",
                "stdout": "",
                "stderr": f"Backend unreachable: {str(e)}",
                "runtime_ms": 0,
                "test_results": []
            }

    def get_coach_feedback(
        self,
        problem_id: str,
        code: str,
        language: str = "python",
        request_type: str = "debug",
        hint_level: int = 1,
        user_id: Optional[str] = "student_demo"
    ) -> Dict[str, Any]:
        """Query the RAG-powered AI Coach for structured line-level guidance."""
        payload = {
            "problem_id": problem_id,
            "code": code,
            "language": language,
            "request_type": request_type,
            "hint_level": hint_level,
            "user_id": user_id
        }
        try:
            res = requests.post(
                f"{self.base_url}/api/coach",
                json=payload,
                timeout=25.0  # Longer timeout for AI coach response
            )
            if res.status_code == 200:
                return res.json()
            return {
                "status": "error",
                "error": f"API Error (HTTP {res.status_code}): {res.text}",
                "response": None
            }
        except Exception as e:
            return {
                "status": "error",
                "error": f"AI Coach Service Unreachable: {str(e)}",
                "response": None
            }

    def search_rag(
        self,
        query: str,
        topic: Optional[str] = None,
        pattern: Optional[str] = None,
        top_k: int = 5
    ) -> Dict[str, Any]:
        """Perform semantic search against RAG knowledge base."""
        payload = {
            "query": query,
            "topic": topic,
            "pattern": pattern,
            "top_k": top_k
        }
        try:
            res = requests.post(
                f"{self.base_url}/api/rag/search",
                json=payload,
                timeout=self.timeout
            )
            if res.status_code == 200:
                return res.json()
            return {"results": [], "context": "", "sources": [], "error": f"HTTP {res.status_code}"}
        except Exception as e:
            return {"results": [], "context": "", "sources": [], "error": str(e)}
