import heapq
class Solution:
    """
    Time: 82% (136ms)
    """
    def missingNumber(self, nums: List[int]) -> int:
        expected = len(nums) * (len(nums)+1) // 2
        actual = sum(nums)
        return expected - actual
