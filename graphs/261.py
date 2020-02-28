class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # dfs and if a cycle exists it is not a tree
        graph = [[] for _ in range(n)]
        visited = [0 for _ in range(n)]

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(graph,visited,parent,i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True

            visited[i] = -1
            for neighbor in graph[i]:
                if neighbor == parent: continue

                elif not dfs(graph,visited,i,neighbor):
                    return False
            visited[i] = 1
            return True
        # Run DFS starting at 0
        if not dfs(graph,visited,-1,0): return False

        # Check for unconnected components
        if 0 in visited: return False

        return True
