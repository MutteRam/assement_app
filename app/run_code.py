import requests


import requests


def normalize_output(text):
    if text is None:
        return ""

    text = str(text)

    # Convert Windows line endings to normal newline
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    # Remove leading/trailing spaces from each line
    lines = [line.strip() for line in text.split("\n")]

    # Remove empty lines at beginning/end
    while lines and lines[0] == "":
        lines.pop(0)

    while lines and lines[-1] == "":
        lines.pop()

    return "\n".join(lines)


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
        output = normalize_output(data.get("stdout"))

        # Expected output from database
        expected = normalize_output(test.expected_output)

        # Compare normalized output
        passed = output == expected

        results.append({
            "passed": passed,
            "input": test.input_data,
            "output": output,
            "expected": expected,
            "hidden": test.is_hidden,
        })

    return results