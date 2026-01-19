import json
from solution import commonCharacters


def run_tests():
    with open("test.json", "r") as f:
        test_cases = json.load(f)

    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        strings = test["strings"]
        expected = set(test["expected"])

        try:
            result = commonCharacters(strings)
            result_set = set(result) if result else set()

            if result_set == expected:
                print(f"Test {i}: PASSED")
                passed += 1
            else:
                print(f"Test {i}: FAILED")
                print(f"  Input: {strings}")
                print(f"  Expected: {sorted(expected)}")
                print(f"  Got: {sorted(result_set)}")
                failed += 1
        except Exception as e:
            print(f"Test {i}: ERROR - {e}")
            failed += 1

    print(f"\n{'='*40}")
    print(f"Results: {passed}/{passed + failed} tests passed")

    return passed, failed


if __name__ == "__main__":
    run_tests()
