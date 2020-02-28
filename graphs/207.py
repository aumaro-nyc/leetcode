class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Detecting a cycle will indicate an impossible schedule
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]

        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(graph,visited,i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True
            visited[i] = -1
            for neighbor in graph[i]:
                if not dfs(graph,visited,neighbor):
                    return False
            visited[i] = 1
            return True

        for i in range(numCourses):
            if not dfs(graph,visited,i):
                return False
        return True
