import json
from solution import isValidSubsequence

with open("test.json", "r") as f:
    test_cases = json.load(f)

passed = 0
failed = 0

for i, test in enumerate(test_cases, 1):
    array = test["array"]
    sequence = test["sequence"]
    expected = test["expected"]
    result = isValidSubsequence(array, sequence)

    if result == expected:
        passed += 1
        status = "PASS"
    else:
        failed += 1
        status = "FAIL"

    print(f"Test {i:2}: {status} | Expected: {str(expected):5} | Got: {str(result):5} | sequence={sequence}")

print(f"\nResults: {passed} passed, {failed} failed out of {len(test_cases)} tests")
