# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_len = 1
        def depth(node):
            nonlocal max_len
            if not node: return 0
            left = depth(node.left)
            right = depth(node.right)
            max_len = max(max_len, left + right + 1)
            return max(left, right) + 1

        depth(root)
        return max_len - 1
