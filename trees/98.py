# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True

        def check_node(node,lower,upper):
            if not node: return True
            if node.val <= lower or node.val >= upper:
                return False
            return check_node(node.left,lower,node.val) and check_node(node.right,node.val,upper)

        return check_node(root,float('-inf'),float('inf'))
