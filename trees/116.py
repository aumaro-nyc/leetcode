"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        l = []
        w = []
        l.append(root)
        while l:
            c = l.pop(0)
            w.append(c)
            while l:
                tmp = l.pop(0)
                c.next = tmp
                w.append(tmp)
                c = tmp
            while w:
                tmp = w.pop(0)
                if not tmp:
                    continue
                if tmp.left is not None:
                    l.append(tmp.left)
                if tmp.right is not None:
                    l.append(tmp.right)
        return root
