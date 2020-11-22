class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findClosestValueInBst(tree: BST, target: int):
    """
    Find the value in BST that is closest to the target value.

    :param tree:
    :param target:
    :return:
    """
    return _helper(tree, target, float('inf'))


def _helper(node: BST, target: int, diff: int):
    """

    :param node:
    :param target:
    :param diff:
    :return:
    """
    if node is None:
        return diff
    val = node.value
    new_diff = abs(val - target)
    if abs(diff - target) > new_diff:
        diff = val
    a = _helper(node.left, target, diff)
    b = _helper(node.right, target, diff)
    if abs(a - target) > abs(b - target):
        return b
    return a
