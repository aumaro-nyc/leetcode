"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        Return deep copy of a graph given a starting
        node.
        """
        if not node:
            return None
        node_map = {}
        def dfs(node):
            if node not in node_map:
                node_map[node] = Node(node.val)
            for n in node.neighbors:
                if n in node_map:
                    node_map[node].neighbors.append(node_map[n])
                if n not in node_map:
                    dfs(n)
                    node_map[node].neighbors.append(node_map[n])
        dfs(node)
        return node_map[node]
