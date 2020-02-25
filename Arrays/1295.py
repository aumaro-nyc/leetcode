class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                result += 1
        return result
