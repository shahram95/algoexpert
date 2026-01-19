import json
from solution import BinaryTree, evaluateExpressionTree


def build_tree(tree_data):
    """Build a BinaryTree from JSON node data."""
    nodes = {node["id"]: node for node in tree_data["nodes"]}
    built_nodes = {}

    def build_node(node_id):
        if node_id is None:
            return None
        if node_id in built_nodes:
            return built_nodes[node_id]

        node_data = nodes[node_id]
        left = build_node(node_data["left"])
        right = build_node(node_data["right"])
        tree_node = BinaryTree(node_data["value"], left, right)
        built_nodes[node_id] = tree_node
        return tree_node

    return build_node(tree_data["root"])


def run_tests():
    with open("test.json", "r") as f:
        test_cases = json.load(f)

    passed = 0
    failed = 0

    for i, test_case in enumerate(test_cases, 1):
        tree = build_tree(test_case["tree"])
        expected = test_case["expected"]
        result = evaluateExpressionTree(tree)

        if result == expected:
            print(f"Test {i}: PASSED")
            passed += 1
        else:
            print(f"Test {i}: FAILED (expected {expected}, got {result})")
            failed += 1

    print(f"\n{'='*40}")
    print(f"Results: {passed}/{passed + failed} tests passed")
    if failed == 0:
        print("All tests passed!")
    else:
        print(f"{failed} test(s) failed.")


if __name__ == "__main__":
    run_tests()
