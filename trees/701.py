# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        def helper(root, val):
            if val < root.val:
                if not root.left:
                    root.left = TreeNode(val)
                    return root
                else:
                    return self.insertIntoBST(root.left, val)
            if val > root.val:
                if not root.right:
                    root.right = TreeNode(val)
                    return root
                else:
                    return self.insertIntoBST(root.right, val)

        helper(root, val)
        return root
