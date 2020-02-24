class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if nums == []: return 0
        i = 1
        max = 1
        count = 1
        while i < len(nums):
            if nums[i] > nums[i - 1]:
                count += 1
                i += 1
            else:
                if count > max:
                    max = count
                count = 1
                i += 1
        if count > max:
            max = count
        return max
