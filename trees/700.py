# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        Search a BST for a value and return it if found
        """
        if not root: return
        while root:
            if root.val == val: return root
            root = root.left if val < root.val else root.right
