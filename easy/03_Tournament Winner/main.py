import json
from solution import tournamentWinner


def run_tests():
    with open("test.json", "r") as f:
        test_cases = json.load(f)

    passed = 0
    total = len(test_cases)

    for i, test in enumerate(test_cases, 1):
        competitions = test["competitions"]
        results = test["results"]
        expected = test["expected"]

        try:
            actual = tournamentWinner(competitions, results)
            if actual == expected:
                print(f"Test {i}: PASSED")
                passed += 1
            else:
                print(f"Test {i}: FAILED - Expected '{expected}', got '{actual}'")
        except Exception as e:
            print(f"Test {i}: ERROR - {e}")

    print(f"\nResults: {passed}/{total} test cases passed")


if __name__ == "__main__":
    run_tests()
