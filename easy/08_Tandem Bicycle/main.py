import json
from solution import tandemBicycle


def run_tests():
    with open("test.json", "r") as f:
        tests = json.load(f)

    passed = 0
    failed = 0

    for i, test in enumerate(tests, 1):
        red = test["redShirtSpeeds"][:]
        blue = test["blueShirtSpeeds"][:]
        fastest = test["fastest"]
        expected = test["expected"]

        result = tandemBicycle(red, blue, fastest)

        if result == expected:
            passed += 1
            status = "PASSED"
        else:
            failed += 1
            status = "FAILED"

        print(f"Test {i}: {status}")
        if status == "FAILED":
            print(f"  Input: red={test['redShirtSpeeds']}, blue={test['blueShirtSpeeds']}, fastest={fastest}")
            print(f"  Expected: {expected}, Got: {result}")

    print(f"\nResults: {passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()
