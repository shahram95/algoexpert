def findClosestValueInBst(tree, target):
    closest = tree.value
    currentNode = tree

    while currentNode is not None:
        if abs(target-currentNode.value) < abs(target-closest):
            closest = currentNode.value
        
        if currentNode.value > target:
            currentNode = currentNode.left
        elif currentNode.value < target:
            currentNode = currentNode.right
        else:
            break

    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
