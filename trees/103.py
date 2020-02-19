# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return None

        result = []
        level = []
        waiting = []
        zigzag = True
        result.append([root.val])
        level.append(root.left)
        level.append(root.right)

        while len(level) != 0:
            c = []
            while len(level) != 0:
                tmp = level.pop(0)
                if tmp is None:
                    continue
                c.append(tmp.val)
                waiting.append(tmp)
            if len(c) != 0:
                if zigzag:
                    result.append(list(reversed(c)))
                    zigzag = False
                else:
                    result.append(c)
                    zigzag = True
            while len(waiting) != 0:
                tmp = waiting.pop(0)
                if tmp.left is not None:
                    level.append(tmp.left)
                if tmp.right is not None:
                    level.append(tmp.right)
        return result
