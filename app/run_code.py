import requests


def execute_code(code, test_cases):
    results = []

    for test in test_cases:

        response = requests.post(
            "https://ce.judge0.com/submissions/?base64_encoded=false&wait=true",
            json={
                "source_code": code,
                "language_id": 71,
                "stdin": test.input_data,
            },
            timeout=15
        )

        data = response.json()

        # User's program output
        output = (data.get("stdout") or "").strip()

        # Expected output from database
        expected = (test.expected_output or "").strip()

        # Compare output
        passed = output == expected

        results.append({
            "passed": passed,
            "input": test.input_data,
            "output": output,
            "expected": expected,
            "hidden": test.is_hidden,
        })

    return results