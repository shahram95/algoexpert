import json
from solution import nodeDepths, BinaryTree


def build_tree(tree_data):
    """Build a BinaryTree from JSON tree data."""
    nodes_data = tree_data["nodes"]
    root_id = tree_data["root"]

    # Create a map of id -> node data
    node_map = {node["id"]: node for node in nodes_data}

    # Create BinaryTree nodes
    tree_nodes = {}
    for node_data in nodes_data:
        tree_nodes[node_data["id"]] = BinaryTree(node_data["value"])

    # Link nodes together
    for node_data in nodes_data:
        node = tree_nodes[node_data["id"]]
        if node_data["left"]:
            node.left = tree_nodes[node_data["left"]]
        if node_data["right"]:
            node.right = tree_nodes[node_data["right"]]

    return tree_nodes[root_id]


def run_tests():
    with open("test.json", "r") as f:
        tests = json.load(f)

    passed = 0
    failed = 0

    for i, test in enumerate(tests, 1):
        tree = build_tree(test["tree"])
        expected = test["expected"]
        result = nodeDepths(tree)

        if result == expected:
            print(f"Test {i}: PASSED")
            passed += 1
        else:
            print(f"Test {i}: FAILED (expected {expected}, got {result})")
            failed += 1

    print(f"\n{passed}/{passed + failed} tests passed")


if __name__ == "__main__":
    run_tests()
