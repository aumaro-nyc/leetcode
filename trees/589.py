"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        """
        Iterative inorder traversal of an N-ary tree
        """
        if not root: return
        result = []
        stack = []
        stack.append(root)
        while stack:
            current = stack.pop()
            result.append(current.val)
            i = len(current.children) - 1
            while i >= 0:
                stack.append(current.children[i])
                i -= 1
        return result

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return
        result = []
        stack = [root]
        while stack:
            current = stack.pop()
            result.append(current.val)
            stack.extend(current.children)

        return result[::-1]
