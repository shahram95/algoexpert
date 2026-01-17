import json
from solution import productSum


def run_tests():
    with open("test.json", "r") as f:
        data = json.load(f)

    tests = data["tests"]
    passed = 0
    failed = 0

    for i, test in enumerate(tests, 1):
        array = test["array"]
        expected = test["expected"]
        result = productSum(array)

        if result == expected:
            print(f"Test {i}: PASSED")
            passed += 1
        else:
            print(f"Test {i}: FAILED")
            print(f"  Input: {array}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")
            failed += 1

    print(f"\n{passed}/{passed + failed} tests passed")


if __name__ == "__main__":
    run_tests()
