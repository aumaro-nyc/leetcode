class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        if n == 0: return 0

        def dfs(graph,visited,node):
            if visited[node] == -1: return
            visited[node] = -1
            for neighbor in graph[node]:
                dfs(graph,visited,neighbor)
            return

        graph = [[] for _ in range(n)]
        visited = [0 for _ in range(n)]
        count = 1

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        dfs(graph,visited,0)
        for i in range(n):
            if visited[i] == -1:
                continue
            dfs(graph,visited,i)
            count += 1
        return count
