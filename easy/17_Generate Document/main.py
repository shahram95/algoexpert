import json
from solution import generateDocument


def run_tests():
    with open("test.json", "r") as f:
        tests = json.load(f)

    passed = 0
    failed = 0

    for i, test in enumerate(tests, 1):
        characters = test["characters"]
        document = test["document"]
        expected = test["expected"]

        result = generateDocument(characters, document)

        if result == expected:
            passed += 1
            print(f"Test {i}: PASSED")
        else:
            failed += 1
            print(f"Test {i}: FAILED")
            print(f"  Characters: {repr(characters)}")
            print(f"  Document: {repr(document)}")
            print(f"  Expected: {expected}, Got: {result}")

    print(f"\n{'='*40}")
    print(f"Results: {passed}/{len(tests)} tests passed")
    if failed == 0:
        print("All tests passed!")
    else:
        print(f"{failed} test(s) failed.")


if __name__ == "__main__":
    run_tests()
