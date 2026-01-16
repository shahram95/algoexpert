import json
from solution import sortedSquaredArray


def main():
    # Load test cases
    with open("test.json", "r") as f:
        test_cases = json.load(f)

    passed = 0
    failed = 0

    print("=" * 60)
    print("Sorted Squared Array - Test Results")
    print("=" * 60)

    for i, test in enumerate(test_cases, 1):
        array = test["array"]
        expected = test["expected"]
        result = sortedSquaredArray(array.copy())  # copy to avoid mutation

        if result == expected:
            passed += 1
            status = "PASS"
        else:
            failed += 1
            status = "FAIL"

        print(f"\nTest Case {i}: {status}")
        print(f"  Input:    {array}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")

    print("\n" + "=" * 60)
    print(f"Results: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 60)

    if failed == 0:
        print("All tests passed!")
    else:
        print(f"{failed} test(s) failed.")


if __name__ == "__main__":
    main()
