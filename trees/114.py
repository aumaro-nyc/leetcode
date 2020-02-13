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
        if not root:
            return None
        self.queue = []

        def helper(root):
            """
            Performs pre-order traversal and appends nodes to Queue
            """
            if not root:
                return None
            self.queue.append(root)
            helper(root.left)
            helper(root.right)
        
        helper(root)
        c = self.queue.pop(0)
        c.left = None
        while self.queue:
            tmp = self.queue.pop(0)
            tmp.left = None
            c.right = tmp
            c = tmp
