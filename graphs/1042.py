import collections

class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        graph = self.createGraph(N,paths)
        flowers = {i:0 for i in range(N+1)}
        for node in graph:
            picks = set(range(1,5))
            for adj in graph[node]:
                if flowers[adj] != 0 and flowers[adj] in picks:
                    picks.remove(flowers[adj])
            flowers[node] = picks.pop()
        return [flowers[x] if flowers[x] != 0 else 1 for x in range(1,N+1)]

    def createGraph(self, N, paths):
        graph = collections.defaultdict(list)
        for x, y in paths:
            graph[x].append(y)
            graph[y].append(x)
        return graph
