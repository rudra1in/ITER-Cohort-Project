import ast
from typing import Dict, Any, List

def check_syntax_locally(code: str) -> Dict[str, Any]:
    """
    Parses Python code using the standard library `ast` module.
    Returns a dict compatible with backend's CodeAnalysisResponse.
    """
    if not code.strip():
        return {"valid": True, "issues": []}
    
    try:
        ast.parse(code)
        return {"valid": True, "issues": []}
    except SyntaxError as e:
        # Extract syntax error details
        line = e.lineno or 1
        column = e.offset or 1
        msg = e.msg or "Syntax error"
        
        # Clean up common messages
        if "expected" in msg.lower() and not msg.startswith("SyntaxError"):
            msg = f"SyntaxError: {msg}"
            
        return {
            "valid": False,
            "issues": [
                {
                    "line": line,
                    "column": column,
                    "severity": "error",
                    "type": "SyntaxError",
                    "message": f"Line {line} | {msg}"
                }
            ]
        }
    except Exception as e:
        return {
            "valid": False,
            "issues": [
                {
                    "line": 1,
                    "column": 1,
                    "severity": "error",
                    "type": "ParserError",
                    "message": f"Failed to parse code: {str(e)}"
                }
            ]
        }
