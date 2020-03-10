class Solution:
    # 52 - 56 ms: beat 86%
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        mapp = {}
        sorted_input = sorted(nums)
        i = 0
        while i < len(sorted_input):
            mapp[sorted_input[i]] = i
            if i+1 < len(sorted_input) and sorted_input[i+1] == sorted_input[i]:
                while i+1 < len(sorted_input) and sorted_input[i+1] == sorted_input[i]:
                    i += 1
            i += 1
        for n in nums:
            result.append(mapp[n])
        return result
