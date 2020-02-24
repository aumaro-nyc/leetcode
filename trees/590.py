"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def __init__(self):
        self.result = []

    def postorder(self, root: 'Node') -> List[int]:
        if not root: return
        for ch in root.children:
            self.postorder(ch)
        self.result.append(root.val)
        return self.result
