import json
from solution import runLengthEncoding


def run_tests():
    with open("test.json", "r") as f:
        tests = json.load(f)

    passed = 0
    failed = 0

    for i, test in enumerate(tests, 1):
        input_str = test["string"]
        expected = test["expected"]
        result = runLengthEncoding(input_str)

        if result == expected:
            print(f"Test {i}: PASSED")
            passed += 1
        else:
            print(f"Test {i}: FAILED")
            print(f"  Input:    {repr(input_str)}")
            print(f"  Expected: {repr(expected)}")
            print(f"  Got:      {repr(result)}")
            failed += 1

    print(f"\n{'='*40}")
    print(f"Results: {passed}/{len(tests)} tests passed")
    if failed == 0:
        print("All tests passed!")
    else:
        print(f"{failed} test(s) failed.")


if __name__ == "__main__":
    run_tests()
