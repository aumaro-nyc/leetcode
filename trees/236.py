# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Find the lowest common ancestor of two nodes in a Binary Tree
        """
        self.lca = None

        def recurse_tree(node, p, q):
            """
            Recursive function to check left and right subtrees for p and q,
            returning a boolean
            """
            if not node: return False
            left = recurse_tree(node.left,p,q)
            right = recurse_tree(node.right,p,q)
            mid = node.val == p.val or node.val == q.val
            if left + right + mid >= 2:
                self.lca = node
            return left or right or mid

        recurse_tree(root,p,q)
        return self.lca
