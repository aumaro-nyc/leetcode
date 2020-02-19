# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left and not root.right: return 1
        elif root.left != None and root.right != None:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        elif root.right is None:
            return 1 + self.maxDepth(root.left)
        else:
            return 1 + self.maxDepth(root.right)
