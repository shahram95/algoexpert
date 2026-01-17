import json
from solution import minimumWaitingTime

def run_tests():
    with open("test.json", "r") as f:
        tests = json.load(f)

    passed = 0
    failed = 0

    for i, test in enumerate(tests, 1):
        queries = test["queries"].copy()  # Copy to avoid mutation issues
        expected = test["expected"]
        result = minimumWaitingTime(queries)

        if result == expected:
            passed += 1
            print(f"Test {i}: PASSED")
        else:
            failed += 1
            print(f"Test {i}: FAILED - Input: {test['queries']}, Expected: {expected}, Got: {result}")

    print(f"\n{'='*40}")
    print(f"Results: {passed}/{len(tests)} tests passed")
    if failed == 0:
        print("All tests passed!")
    else:
        print(f"{failed} test(s) failed.")

if __name__ == "__main__":
    run_tests()
