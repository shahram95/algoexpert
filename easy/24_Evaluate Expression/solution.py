# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    if tree.value >= 0:
        return tree.value
    
    left_value = evaluateExpressionTree(tree.left)
    right_value = evaluateExpressionTree(tree.right)

    if tree.value == -1:
        return left_value + right_value
    elif tree.value == -2:
        return left_value - right_value
    elif tree.value == -3:
        return int(left_value/right_value)
    elif tree.value == -4:
        return left_value*right_value