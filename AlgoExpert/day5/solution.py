# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.max_dist = 0
        self.helper(root)
        return self.max_dist - 1

    def helper(self, root):
        if root is None:
            return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        self.max_dist = max(self.max_dist, l + r + 1)
        return max(l, r) + 1
