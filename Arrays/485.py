class Solution:
    """
    Time: 93% (364ms)
    """
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        count = 0
        for ele in nums:
            if ele == 0:
                if count > max_len:
                    max_len = count
                count = 0
            else:
                count += 1
        if count > max_len:
            max_len = count
        return max_len
