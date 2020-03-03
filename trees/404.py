# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.sum = 0

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0
        self.getSum(root)
        return self.sum

    def getSum(self, root):
        if not root: return
        if self.isLeaf(root.left):
            self.sum += root.left.val
        self.sumOfLeftLeaves(root.left)
        self.sumOfLeftLeaves(root.right)

    def isLeaf(self, node):
        try:
            return node.left is None and node.right is None
        except AttributeError:
            return False
