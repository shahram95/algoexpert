import json
from solution import twoNumberSum


def main():
    with open("test.json", "r") as f:
        test_cases = json.load(f)

    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        array = test["array"]
        target_sum = test["targetSum"]
        expected = test["expected"]
        result = twoNumberSum(array, target_sum)

        # Compare sorted lists since order doesn't matter
        match = sorted(result) == sorted(expected)

        status = "PASS" if match else "FAIL"
        if match:
            passed += 1
        else:
            failed += 1

        print(f"Test {i}: {status}")
        print(f"  Input: array={array}, targetSum={target_sum}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}\n")

    print(f"Results: {passed}/{len(test_cases)} passed, {failed} failed")


if __name__ == "__main__":
    main()
