class Solution:
    """
    Given an array of 2n integers, your task is to group these integers
    into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes
    sum of min(ai, bi) for all i from 1 to n as large as possible.

    Time: 51% (296ms)
    """
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        i = 0
        while i < len(nums):
            total += nums[i]
            i += 2
        return total
