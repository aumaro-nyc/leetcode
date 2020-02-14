# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Recursively compute the lowest common ancestor of two nodes in a BST
        """
        if not root:
            return None

        upper = p if p.val >= q.val else q
        lower = p if p.val < q.val else q

        if root.val >= lower.val and root.val <= upper.val:
            return root
        elif root.val < lower.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > lower.val:
            return self.lowestCommonAncestor(root.left, p, q)
