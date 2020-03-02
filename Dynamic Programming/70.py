class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        memo = [0] * (n + 1)
        memo[1] = 1
        memo[2] = 2
        i = 3
        while i <= n:
            memo[i] = memo[i-2] + memo[i-1]
            i += 1
        return memo[n]
