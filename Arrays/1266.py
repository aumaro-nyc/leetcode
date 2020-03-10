class Solution:
    """
    More efficient than using i,j pointers and a while loop
    Time: 85% (56ms)
    """
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        for i in range(len(points) - 1):
            result += max(abs(points[i][0] - points[i+1][0]), abs(points[i][1] - points[i+1][1]))
        return result
