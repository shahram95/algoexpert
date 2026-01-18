import json
from solution import semordnilap


def normalize_result(result):
    """Normalize result for comparison (order doesn't matter)."""
    return sorted([sorted(pair) for pair in result])


def run_tests():
    with open("test.json", "r") as f:
        tests = json.load(f)

    passed = 0
    failed = 0

    for i, test in enumerate(tests, 1):
        words = test["words"]
        expected = test["expected"]
        result = semordnilap(words)

        normalized_result = normalize_result(result)
        normalized_expected = normalize_result(expected)

        if normalized_result == normalized_expected:
            passed += 1
            print(f"Test {i}: PASSED")
        else:
            failed += 1
            print(f"Test {i}: FAILED")
            print(f"  Input: {words}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")

    print(f"\n{'='*40}")
    print(f"Results: {passed}/{passed + failed} tests passed")
    if failed == 0:
        print("All tests passed!")
    else:
        print(f"{failed} test(s) failed.")


if __name__ == "__main__":
    run_tests()
