import collections

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        g = collections.defaultdict(list)
        for i in range(len(graph)):
            for edge in graph[i]:
                g[i].append(edge)

        def dfs(node):
            for adj in g[node]:
                if adj in color:
                    if color[adj] == color[node]:
                        return False
                else:
                    color[adj] = 1 - color[node]
                    if not dfs(adj):
                        return False
            return True

        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False
        return True
