import json
from solution import caesarCipherEncryptor


def run_tests():
    with open("test.json", "r") as f:
        tests = json.load(f)

    passed = 0
    failed = 0

    for i, test in enumerate(tests, 1):
        string = test["string"]
        key = test["key"]
        expected = test["expected"]
        result = caesarCipherEncryptor(string, key)

        if result == expected:
            print(f"Test {i}: PASSED")
            passed += 1
        else:
            print(f"Test {i}: FAILED")
            print(f"  Input: string='{string}', key={key}")
            print(f"  Expected: '{expected}'")
            print(f"  Got: '{result}'")
            failed += 1

    print(f"\n{'='*40}")
    print(f"Results: {passed}/{len(tests)} tests passed")
    if failed == 0:
        print("All tests passed!")
    else:
        print(f"{failed} test(s) failed.")


if __name__ == "__main__":
    run_tests()
