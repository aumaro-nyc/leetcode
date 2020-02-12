# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        l,w,result = [],[],[]

        result.append(root.val)
        l.append(root.right)
        l.append(root.left)

        while l:
            first = None

            while l:
                tmp = l.pop(0)
                if not tmp:
                    continue
                if not first:
                    first = tmp
                    result.append(first.val)
                w.append(tmp)

            while w:
                tmp = w.pop(0)
                if tmp.right is not None:
                    l.append(tmp.right)
                if tmp.left is not None:
                    l.append(tmp.left)

        return result
