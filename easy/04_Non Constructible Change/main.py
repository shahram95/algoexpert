import json
from solution import nonConstructibleChange

def run_tests():
    with open("test.json", "r") as f:
        tests = json.load(f)

    passed = 0
    failed = 0

    for i, test in enumerate(tests, 1):
        coins = test["coins"][:]  # Copy to avoid mutation from sort
        expected = test["expected"]
        result = nonConstructibleChange(coins)

        if result == expected:
            print(f"Test {i}: PASSED")
            passed += 1
        else:
            print(f"Test {i}: FAILED - Input: {test['coins']}, Expected: {expected}, Got: {result}")
            failed += 1

    print(f"\n{passed}/{passed + failed} tests passed")
    if failed == 0:
        print("All tests passed!")
    else:
        print(f"{failed} test(s) failed")

if __name__ == "__main__":
    run_tests()
