# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root, running_sum = 0, sums=None):
    if sums is None:
        sums = list()
    if root is None:
        return sums
    
    new_running_sum = running_sum + root.value

    if root.left is None and root.right is None:
        sums.append(new_running_sum)
        return sums
    branchSums(root.left, new_running_sum, sums)
    branchSums(root.right, new_running_sum, sums)
    return sums