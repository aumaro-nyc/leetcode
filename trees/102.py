# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return
        level_q = []
        waiting_q = []
        result = []
        result.append([root.val])
        level_q.append(root.left)
        level_q.append(root.right)

        while level_q:
            curr = []
            while level_q:
                tmp = level_q.pop(0)
                if tmp is None: continue
                curr.append(tmp.val)
                waiting_q.append(tmp)
            if len(curr) != 0:
                result.append(curr)
            while waiting_q:
                tmp = waiting_q.pop(0)
                if tmp.left is not None:
                    level_q.append(tmp.left)
                if tmp.right is not None:
                    level_q.append(tmp.right)
        return result
