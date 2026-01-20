import json
from solution import Node


def build_graph(graph_data):
    """Build the graph from JSON data and return the start node."""
    nodes = {}

    # Create all nodes first
    for node_data in graph_data["nodes"]:
        nodes[node_data["id"]] = Node(node_data["value"])

    # Add children references
    for node_data in graph_data["nodes"]:
        node = nodes[node_data["id"]]
        for child_id in node_data["children"]:
            node.children.append(nodes[child_id])

    return nodes[graph_data["startNode"]]


def run_tests():
    with open("test.json", "r") as f:
        test_cases = json.load(f)

    passed = 0
    total = len(test_cases)

    for i, test_case in enumerate(test_cases, 1):
        start_node = build_graph(test_case["graph"])
        result = start_node.depthFirstSearch([])
        expected = test_case["expected"]

        if result == expected:
            print(f"Test {i}: PASSED")
            passed += 1
        else:
            print(f"Test {i}: FAILED")
            print(f"  Expected: {expected}")
            print(f"  Got:      {result}")

    print(f"\nResults: {passed}/{total} tests passed")


if __name__ == "__main__":
    run_tests()
