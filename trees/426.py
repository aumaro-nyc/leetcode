"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        def traversal(node):
            nonlocal first, last
            if node:
                traversal(node.left)
                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node
                last = node
                traversal(node.right)

        if not root: return
        first = None
        last = None
        traversal(root)
        last.right = first
        first.left = last
        return first
