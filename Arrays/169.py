class Solution:
    """
    Time: 45% (184ms)
    """
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        freq_map = {}
        target = len(nums) // 2 + 1
        for ele in nums:
            if ele not in freq_map:
                freq_map[ele] = 1
            else:
                freq_map[ele] += 1
                if freq_map[ele] == target:
                    return ele
