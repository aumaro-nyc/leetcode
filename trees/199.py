# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        result = []
        level = deque()
        waiting = deque()
        level.append(root)

        while level:
            added = False
            while level:
                temp = level.popleft()
                if not added:
                    result.append(temp.val)
                    added = True
                waiting.append(temp)
            while waiting:
                temp = waiting.popleft()
                if temp.right is not None:
                    level.append(temp.right)
                if temp.left is not None:
                    level.append(temp.left)
        return result
