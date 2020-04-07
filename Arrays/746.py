class Solution:
    """
    Time: 91% (52ms)
    Space: O(1)
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f1 = cost[0]
        f2 = cost[1]
        for i in range(2, len(cost)):
            f1, f2 = f2, cost[i] + min(f1,f2)
        return min(f1, f2)


class Solution:
    """
    Time: 75% (56ms)
    Space: O(n)
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [0] * len(cost)
        memo[0] = cost[0]
        memo[1] = cost[1]
        for i in range(2, len(cost)):
            memo[i] = min(memo[i-1] + cost[i], memo[i-2] + cost[i])
        return min(memo[len(memo) - 1], memo[len(memo) - 2])
