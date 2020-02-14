# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        self.queue = []

        def preorder(root):
            """
            Performs pre-order traversal and appends nodes to Queue
            """
            if not root: return
            self.queue.append(root)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        current = self.queue.pop(0)
        current.left = None
        while self.queue:
            temp = self.queue.pop(0)
            temp.left = None
            current.right = tmp
            current = tmp
