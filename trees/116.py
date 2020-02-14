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
        """
        Populate next pointers to point at the next right hand node
        in the tree.
        """
        if not root: return
        level = []
        waiting = []
        level.append(root)
        while level:
            current = level.pop(0)
            waiting.append(current)
            while level:
                temp = level.pop(0)
                current.next = temp
                waiting.append(temp)
                current = temp
            while waiting:
                temp = waiting.pop(0)
                if not temp: continue
                if temp.left is not None:
                    level.append(temp.left)
                if temp.right is not None:
                    level.append(temp.right)
        return root
