# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Time: 90% (216ms)
    """
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root: return 0
        if root.val < L or root.val > R:
            if root.val < L:
                return self.rangeSumBST(root.right,L,R)
            if root.val > R:
                return self.rangeSumBST(root.left,L,R)
        else:
            return root.val + self.rangeSumBST(root.left,L,R) + self.rangeSumBST(root.right,L,R)
