"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        """
        Returns a deep copy of a singly linked list where
        each node also contains a pointer to a random
        node also in the linked list.
        """

        if not head:
            return None
        node_map = {None:None}

        def dfs(node):
            if node not in node_map:
                node_map[node] = Node(node.val)
            if node.next is None:
                node_map[node].next = None
                node_map[node].random = node_map[node.random]
                return
            if node.next not in node_map:
                dfs(node.next)
            node_map[node].next = node_map[node.next]
            node_map[node].random = node_map[node.random]

        dfs(head)
        return node_map[head]
