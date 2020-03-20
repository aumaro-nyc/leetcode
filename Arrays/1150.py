class Solution:
    """
    Time: 99% (24ms)
    """
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        number_map = {}
        for element in nums:
            if element not in number_map:
                number_map[element] = 1
            else:
                number_map[element] += 1
        if target not in number_map:
            return False
        else:
            return True if number_map[target] > (len(nums) / 2) else False
