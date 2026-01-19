import json
from solution import findClosestValueInBst, BST


def build_tree(tree_data):
    """Build a BST from the JSON tree structure."""
    nodes = {node["id"]: node for node in tree_data["nodes"]}
    bst_nodes = {}

    for node_id, node_data in nodes.items():
        bst_nodes[node_id] = BST(node_data["value"])

    for node_id, node_data in nodes.items():
        if node_data["left"]:
            bst_nodes[node_id].left = bst_nodes[node_data["left"]]
        if node_data["right"]:
            bst_nodes[node_id].right = bst_nodes[node_data["right"]]

    return bst_nodes[tree_data["root"]]


def run_tests():
    with open("test.json", "r") as f:
        data = json.load(f)

    tests = data["tests"]
    passed = 0
    failed = 0

    for test in tests:
        name = test["name"]
        tree = build_tree(test["tree"])
        target = test["target"]
        expected = test["expected"]

        result = findClosestValueInBst(tree, target)

        if result == expected:
            print(f"PASSED: {name} - target={target}, expected={expected}, got={result}")
            passed += 1
        else:
            print(f"FAILED: {name} - target={target}, expected={expected}, got={result}")
            failed += 1

    print(f"\n{'='*50}")
    print(f"Results: {passed}/{passed + failed} tests passed")
    if failed == 0:
        print("All tests passed!")
    else:
        print(f"{failed} test(s) failed")


if __name__ == "__main__":
    run_tests()
