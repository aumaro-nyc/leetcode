"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        """
        Level order traversal of an N-ary tree
        """
        if not root: return []
        level = []
        waiting = []
        result = []
        level.append(root)
        while level:
            current = []
            while level:
                tmp = level.pop(0)
                if not tmp:
                    continue
                current.append(tmp.val)
                waiting.append(tmp)
            if len(current) > 0:
                result.append(current)
            while waiting:
                tmp = waiting.pop(0)
                for ch in tmp.children:
                    level.append(ch)
        return result
