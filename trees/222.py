# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        q = []
        count = 0
        q.append(root)
        while q:
            c = q.pop(0)
            if not c:
                continue
            count += 1
            q.append(c.left)
            q.append(c.right)

        return count
