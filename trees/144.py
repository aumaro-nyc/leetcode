# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Iterative pre-order traversal of a binary tree
        """
        stack = []
        preorder = []
        stack.append(root)

        while stack:
            node = stack.pop()
            if not node: continue
            preorder.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return preorder
