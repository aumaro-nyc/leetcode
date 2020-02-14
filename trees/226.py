# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        Recursively invert a binary tree
        """
        if not root: return
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.right = left
        root.left = right
        return root
