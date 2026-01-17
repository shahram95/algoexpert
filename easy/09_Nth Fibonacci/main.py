import json
from solution import getNthFib


def run_tests():
    with open("test.json", "r") as f:
        tests = json.load(f)

    passed = 0
    failed = 0

    for i, test in enumerate(tests, 1):
        n = test["n"]
        expected = test["expected"]
        result = getNthFib(n)

        if result == expected:
            passed += 1
            print(f"Test {i}: PASSED (n={n}, expected={expected}, got={result})")
        else:
            failed += 1
            print(f"Test {i}: FAILED (n={n}, expected={expected}, got={result})")

    print(f"\n{'='*50}")
    print(f"Results: {passed}/{len(tests)} tests passed")
    if failed == 0:
        print("All tests passed!")
    else:
        print(f"{failed} test(s) failed.")


if __name__ == "__main__":
    run_tests()
