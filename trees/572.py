# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def compare(s_start, t_start):
            if (not s_start) ^ (not t_start): return False
            if not s_start and not t_start: return True
            if s_start.val == t_start.val:
                return compare(s_start.left, t_start.left) and compare(s_start.right, t_start.right)
            else:
                return False

        """
        # Traverse tree checking each node with val == t.val
        # If compare returns true then the function exits with a value of true,
        # otherwise all additional nodes are checked and if no matching
        # subtrees are found then false is returned.
        """
        if not s and not t: return True
        if not s: return False
        if s.val == t.val and compare(s,t):
             return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
