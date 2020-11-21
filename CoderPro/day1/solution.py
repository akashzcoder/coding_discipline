# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# top down recursion solution
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.is_valid_bst(root, float('-inf'), float('inf'))

    def is_valid_bst(self, node, min_left, max_right):
        if node is None:
            return True
        if node.val > min_left and node.val < max_right:
            return True and self.is_valid_bst(node.left, min_left, node.val) and \
                   self.is_valid_bst(node.right, node.val, max_right)


# iterative solution -> replica of top-down recursive
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # inorder traversal
        if root is None:
            return True
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            ele, lower, upper = stack.pop()  # 2
            if not ele:
                continue
            val = ele.val  # 2
            if val <= lower or val >= upper:
                return False
            stack.append((ele.right, val, upper))  # 3, lower: 2, inf
            stack.append((ele.left, lower, val))  # 1, lower: -inf, 2
        return True


# inorder solution
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, inorder = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True