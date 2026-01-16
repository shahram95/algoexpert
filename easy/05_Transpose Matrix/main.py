import json
from solution import transposeMatrix


def main():
    with open("test.json", "r") as f:
        data = json.load(f)

    tests = data["tests"]
    passed = 0
    failed = 0

    for i, test in enumerate(tests, 1):
        matrix = test["matrix"]
        expected = test["expected"]
        result = transposeMatrix(matrix)

        if result == expected:
            print(f"Test {i}: PASSED")
            passed += 1
        else:
            print(f"Test {i}: FAILED")
            print(f"  Input:    {matrix}")
            print(f"  Expected: {expected}")
            print(f"  Got:      {result}")
            failed += 1

    print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")


if __name__ == "__main__":
    main()
