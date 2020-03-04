import collections

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusts = collections.defaultdict(list)
        trusted_by = collections.defaultdict(list)
        for x, y in trust:
            trusts[x].append(y)
            trusted_by[y].append(x)

        for i in range(1,N+1):
            if i not in trusts and len(trusted_by[i]) == N - 1:
                return i
        return -1
