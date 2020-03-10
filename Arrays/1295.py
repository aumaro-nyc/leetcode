class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        """
        More efficient than strlen % 2 and if/elif statement
        Time: 76% (52ms)
        """
        count = 0
        for n in nums:
            if 10 <= n < 100:
                count += 1
            if 1000 <= n < 10000:
                count += 1
            if n == 100000:
                count += 1
        return count
