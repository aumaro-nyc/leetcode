# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = 1
        sum_map = {}
        level_queue = []
        waiting = []
        level_queue.append(root)

        while level_queue:
            total = 0
            while level_queue:
                current = level_queue.pop(0)
                total += current.val
                waiting.append(current)
            sum_map[total] = level
            level += 1
            while waiting:
                temp = waiting.pop(0)
                if temp.left:
                    level_queue.append(temp.left)
                if temp.right:
                    level_queue.append(temp.right)
        return sum_map[max(sum_map)]
