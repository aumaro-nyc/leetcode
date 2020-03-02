# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        max_width = 0
        level = deque()
        waiting = deque()
        level.append(root)

        while level:
            count = 0
            while level and level[0] is None:
                level.popleft()
            while level and level[-1] is None:
                level.pop()
            while level:
                current = level.popleft()
                count += 1
                waiting.append(current)
            if count > max_width:
                max_width = count
            while waiting:
                temp = waiting.popleft()
                if temp is None:
                    level.append(temp)
                    level.append(temp)
                    continue
                level.append(temp.left)
                level.append(temp.right)
        return max_width
