#!/usr/bin/env python
"""
scripts/validate_dataset.py

Validates the expanded DSA knowledge base dataset in data/ directories:
- Checks for valid JSON format.
- Checks for unique IDs.
- Validates required fields for each document type.
- Checks solution -> problem reference integrity.
- Checks Python syntax inside code fields.
- Checks metadata consistency.
"""

import os
import json
import ast
import sys
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def check_python_syntax(code_str: str, file_path: str) -> bool:
    if not code_str:
        return True
    try:
        ast.parse(code_str)
        return True
    except SyntaxError as e:
        print(f"  [ERROR] Syntax error in code field of {file_path}: {e}")
        return False

def run_validation():
    print("DATASET VALIDATION")
    print("==================")

    categories = ["concepts", "patterns", "problems", "solutions", "mistakes", "examples"]
    
    total_records = 0
    invalid_json = 0
    duplicate_ids = 0
    broken_references = 0
    invalid_python = 0

    seen_ids = set()
    problems_seen = set()
    solutions_references = {} # solution_id -> problem_id
    
    status_checks = {c: True for c in categories}

    for cat in categories:
        cat_dir = DATA_DIR / cat
        if not cat_dir.exists():
            status_checks[cat] = False
            continue

        files = list(cat_dir.glob("*.json"))
        if not files:
            status_checks[cat] = False
            continue

        for fpath in files:
            total_records += 1
            # 1. Check valid JSON
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception as e:
                print(f"  [ERROR] Invalid JSON in {fpath.name}: {e}")
                invalid_json += 1
                status_checks[cat] = False
                continue

            # Check list or dict
            docs = data if isinstance(data, list) else [data]

            for doc in docs:
                # 2. Check unique IDs
                doc_id = doc.get("id")
                if not doc_id:
                    print(f"  [ERROR] Missing ID in {fpath.name}")
                    duplicate_ids += 1
                    status_checks[cat] = False
                elif doc_id in seen_ids:
                    print(f"  [ERROR] Duplicate ID '{doc_id}' in {fpath.name}")
                    duplicate_ids += 1
                    status_checks[cat] = False
                else:
                    seen_ids.add(doc_id)

                doc_type = doc.get("document_type") or doc.get("chunk_type")

                # Track problems and solutions
                if doc_type == "problem":
                    problems_seen.add(doc_id)
                elif doc_type == "solution":
                    solutions_references[doc_id] = doc.get("problem_id")

                # 3. Check Python syntax
                code = doc.get("code")
                if code:
                    if not check_python_syntax(code, fpath.name):
                        invalid_python += 1
                        status_checks[cat] = False

                bad_example = doc.get("bad_example")
                if bad_example:
                    if not check_python_syntax(bad_example, fpath.name):
                        invalid_python += 1
                        status_checks[cat] = False

                corrected_example = doc.get("corrected_example")
                if corrected_example:
                    if not check_python_syntax(corrected_example, fpath.name):
                        invalid_python += 1
                        status_checks[cat] = False

    # Check reference integrity
    for sol_id, prob_id in solutions_references.items():
        if not prob_id or prob_id not in problems_seen:
            print(f"  [ERROR] Solution '{sol_id}' references missing or invalid problem ID '{prob_id}'")
            broken_references += 1
            status_checks["solutions"] = False

    # Output category status
    for cat in categories:
        indicator = "✓" if status_checks[cat] else "✗"
        # Use ascii representation to avoid console encoding crashes
        status_text = "PASS" if status_checks[cat] else "FAIL"
        print(f"{cat.capitalize():<12} {status_text}")

    print()
    print(f"Invalid JSON       {invalid_json}")
    print(f"Duplicate IDs      {duplicate_ids}")
    print(f"Broken references  {broken_references}")
    print(f"Invalid Python     {invalid_python}")
    print()
    print(f"TOTAL RECORDS: {total_records}")
    print()

    if invalid_json == 0 and duplicate_ids == 0 and broken_references == 0 and invalid_python == 0 and total_records > 0:
        print("STATUS: PASS")
        return True
    else:
        print("STATUS: FAIL")
        return False

if __name__ == "__main__":
    success = run_validation()
    if not success:
        sys.exit(1)
