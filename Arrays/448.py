class Solution:
    """
    Time: 86% (364ms)
    """
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        full_set = set(range(1,len(nums) + 1))
        seen_set = set()
        result = []
        for n in nums:
            if n not in seen_set:
                seen_set.add(n)
        for n in full_set:
            if n not in seen_set:
                result.append(n)
        return result
