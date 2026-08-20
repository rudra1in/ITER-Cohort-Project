import os
import subprocess
import tempfile
import time

from config import (
    MAX_OUTPUT_LENGTH,
    PYTHON_EXECUTABLE,
)


def _truncate_output(
    output: str
) -> str:

    if not output:
        return ""

    if len(output) <= MAX_OUTPUT_LENGTH:
        return output

    return (
        output[:MAX_OUTPUT_LENGTH]
        + "\n...[output truncated]"
    )


def execute_python(
    code: str,
    timeout: int
) -> dict:

    temp_file = None

    start_time = time.perf_counter()

    try:

        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".py",
            delete=False,
            encoding="utf-8"
        ) as file:

            file.write(code)

            temp_file = file.name

        result = subprocess.run(
            [
                PYTHON_EXECUTABLE,
                temp_file
            ],
            capture_output=True,
            text=True,
            timeout=timeout
        )

        runtime_ms = int(
            (time.perf_counter() - start_time)
            * 1000
        )

        stdout = _truncate_output(
            result.stdout
        )

        stderr = _truncate_output(
            result.stderr
        )

        if result.returncode == 0:

            status = "success"

        else:

            status = "runtime_error"

        return {
            "status": status,
            "stdout": stdout,
            "stderr": stderr,
            "return_code": result.returncode,
            "runtime_ms": runtime_ms
        }

    except subprocess.TimeoutExpired:

        return {
            "status": "timeout",
            "stdout": "",
            "stderr": (
                "Execution exceeded "
                f"{timeout} seconds."
            ),
            "return_code": -1,
            "runtime_ms": int(
                (time.perf_counter() - start_time)
                * 1000
            )
        }

    except Exception as error:

        return {
            "status": "executor_error",
            "stdout": "",
            "stderr": str(error),
            "return_code": -1,
            "runtime_ms": int(
                (time.perf_counter() - start_time)
                * 1000
            )
        }

    finally:

        if (
            temp_file
            and os.path.exists(temp_file)
        ):
            try:
                os.remove(temp_file)
            except OSError:
                pass


import json


def execute_python_with_tests(
    code: str,
    test_cases: list[dict],
    timeout: int
) -> dict:

    """
    Development implementation.

    The expected student solution should expose
    a function called `solution`.

    Example:

        def solution(nums, target):
            ...

    Each test case should contain:

        {
            "input": [...],
            "expected_output": [...]
        }
    """

    results = []

    for test_case in test_cases:

        input_data = test_case.get(
            "input"
        )

        expected = test_case.get(
            "expected_output"
        )

        # Create a temporary runner that imports
        # the student's solution file.

        runner_code = f"""
{code}

import json

_input = {repr(input_data)}

try:

    if isinstance(_input, dict):
        _result = solution(**_input)

    elif isinstance(_input, (list, tuple)):
        _result = solution(*_input)

    else:
        _result = solution(_input)

    print(json.dumps(_result))

except Exception as _error:

    print(
        "DSA_COACH_RUNTIME_ERROR:"
        + type(_error).__name__
        + ":"
        + str(_error)
    )
"""

        execution = execute_python(
            runner_code,
            timeout
        )

        actual_output = None

        if execution["status"] == "success":

            try:

                actual_output = json.loads(
                    execution["stdout"].strip()
                )

            except json.JSONDecodeError:

                actual_output = (
                    execution["stdout"].strip()
                )

        passed = (
            execution["status"] == "success"
            and actual_output == expected
        )

        error = None

        if execution["status"] != "success":

            error = execution["stderr"]

        elif not passed:

            error = (
                "Wrong answer: "
                "actual output does not "
                "match expected output."
            )

        results.append(
            {
                "passed": passed,
                "input": input_data,
                "expected_output": expected,
                "actual_output": actual_output,
                "error": error,
                "execution_status": execution["status"],
            }
        )

        # Stop after first failing test.
        # This makes debugging easier.

        if not passed:
            break

    # Determine overall status, propagating
    # timeout and runtime_error from inner
    # execution rather than collapsing to
    # "failed".

    if results and all(
        result["passed"]
        for result in results
    ):
        overall_status = "accepted"
    else:
        # Check if the failure was caused by
        # a timeout or runtime error so that
        # the graph routing can distinguish
        # these cases.
        last = results[-1] if results else {}
        exec_status = last.get(
            "execution_status", ""
        )
        if exec_status == "timeout":
            overall_status = "timeout"
        elif exec_status in {
            "runtime_error",
            "executor_error",
        }:
            overall_status = exec_status
        else:
            overall_status = "failed"

    return {
        "status": overall_status,
        "test_results": results
    }