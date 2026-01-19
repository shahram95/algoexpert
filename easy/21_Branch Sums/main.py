import json
from solution import BinaryTree, branchSums


def build_tree(tree_data):
    """Build a BinaryTree from the JSON representation."""
    nodes = tree_data["nodes"]
    root_id = tree_data["root"]

    # Create a map of id -> node data
    node_map = {node["id"]: node for node in nodes}

    # Create a map of id -> BinaryTree node
    tree_nodes = {}

    def get_or_create_node(node_id):
        if node_id is None:
            return None
        if node_id in tree_nodes:
            return tree_nodes[node_id]

        node_data = node_map[node_id]
        tree_node = BinaryTree(node_data["value"])
        tree_nodes[node_id] = tree_node

        tree_node.left = get_or_create_node(node_data["left"])
        tree_node.right = get_or_create_node(node_data["right"])

        return tree_node

    return get_or_create_node(root_id)


def run_tests():
    """Load tests from test.json and run them against the solution."""
    with open("test.json", "r") as f:
        test_cases = json.load(f)

    passed = 0
    failed = 0

    for i, test_case in enumerate(test_cases, 1):
        tree = build_tree(test_case["tree"])
        expected = test_case["expected"]

        try:
            result = branchSums(tree)
            if result == expected:
                print(f"Test {i}: PASSED")
                passed += 1
            else:
                print(f"Test {i}: FAILED")
                print(f"  Expected: {expected}")
                print(f"  Got:      {result}")
                failed += 1
        except Exception as e:
            print(f"Test {i}: ERROR - {e}")
            failed += 1

    print(f"\n{'='*40}")
    print(f"Results: {passed}/{passed + failed} tests passed")

    if failed == 0:
        print("All tests passed!")
    else:
        print(f"{failed} test(s) failed.")


if __name__ == "__main__":
    run_tests()
