# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:

        nearest = root.val
        while root:
            nearest = min(root.val, nearest, key=lambda x: abs(target - x))
            root = root.left if target < root.val else root.right

        return nearest
