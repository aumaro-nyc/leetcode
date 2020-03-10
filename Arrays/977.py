class Solution:
    """
    Given an array of integers A sorted in non-decreasing order,
    return an array of the squares of each number, also in sorted
    non-decreasing order.

    Time: 65% (240ms)
    """
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([x ** 2 for x in A])
