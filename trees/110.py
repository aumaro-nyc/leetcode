# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        Checks if a binary tree is height balanced. (No leaves differ in
        height by more than 1)
        """
        if not root: return True
        left = self.height(root.left)
        right = self.height(root.right)
        if abs(left - right) > 1: return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


    def height(self, node):
        """ Helper function to calculate maximum subtree height """
        if not node: return 0
        return 1 + max(self.height(node.left), self.height(node.right))
