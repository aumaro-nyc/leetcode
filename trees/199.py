# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        Returns a list containing the 'right side view' of a Binary
        tree.
        """
        if not root: return []
        level,waiting,result = [],[],[]
        result.append(root.val)
        level.append(root.right)
        level.append(root.left)
        
        while level:
            first = None
            while level:
                temp = level.pop(0)
                if not temp: continue
                if not first:
                    first = temp
                    result.append(first.val)
                waiting.append(temp)
            while waiting:
                temp = waiting.pop(0)
                if temp.right is not None:
                    level.append(temp.right)
                if temp.left is not None:
                    level.append(temp.left)

        return result
