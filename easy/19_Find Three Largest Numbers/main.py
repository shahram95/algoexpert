import json
from solution import findThreeLargestNumbers


def run_tests():
    with open("test.json", "r") as f:
        tests = json.load(f)

    passed = 0
    failed = 0

    for i, test in enumerate(tests, 1):
        array = test["array"]
        expected = test["expected"]
        result = findThreeLargestNumbers(array.copy())

        if result == expected:
            print(f"Test {i}: PASSED")
            passed += 1
        else:
            print(f"Test {i}: FAILED")
            print(f"  Input:    {test['array']}")
            print(f"  Expected: {expected}")
            print(f"  Got:      {result}")
            failed += 1

    print(f"\n{'='*40}")
    print(f"Results: {passed}/{passed + failed} tests passed")
    if failed == 0:
        print("All tests passed!")
    else:
        print(f"{failed} test(s) failed.")


if __name__ == "__main__":
    run_tests()
