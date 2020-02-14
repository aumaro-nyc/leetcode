# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        """
        Performs BFS to count total number of nodes in a binary tree
        """
        queue = []
        count = 0
        queue.append(root)
        while queue:
            current = queue.pop(0)
            if not current: continue
            count += 1
            queue.append(c.left)
            queue.append(c.right)
        return count
