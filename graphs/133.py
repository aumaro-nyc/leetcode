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
            """
            Depth First Search utility function to traverse graph and populate
            node_map with copies of each original node
            """
            if node not in node_map:
                node_map[node] = Node(node.val)
            for neighbor in node.neighbors:
                if neighbor in node_map:
                    node_map[node].neighbors.append(node_map[neighbor])
                else:
                    dfs(neighbor)
                    node_map[node].neighbors.append(node_map[neighbor])

        dfs(node)
        return node_map[node]
