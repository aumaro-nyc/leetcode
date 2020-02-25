class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i,j = 0,1
        result = []
        while j < len(nums):
            result += ([nums[j]] * nums[i])
            i += 2
            j += 2
        return result
