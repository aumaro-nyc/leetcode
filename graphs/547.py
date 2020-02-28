class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:

        def dfs(graph, visited, i):
            for j in range(len(M)):
                if M[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(M,visited,j)

        visited = [0 for _ in range(len(M))]
        count = 0
        for i in range(len(M)):
            if visited[i] == 0:
                dfs(M,visited,i)
                count += 1
        return count
