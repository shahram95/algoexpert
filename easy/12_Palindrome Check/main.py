import json
from solution import isPalindrome


def run_tests():
    with open("test.json", "r") as f:
        tests = json.load(f)

    passed = 0
    failed = 0

    for i, test in enumerate(tests, 1):
        string = test["string"]
        expected = test["expected"]

        result = isPalindrome(string)

        if result == expected:
            passed += 1
            print(f"Test {i}: PASSED")
        else:
            failed += 1
            print(f"Test {i}: FAILED - Expected {expected}, got {result}")

    print(f"\nResults: {passed}/{len(tests)} tests passed")
    return passed == len(tests)


if __name__ == "__main__":
    run_tests()
