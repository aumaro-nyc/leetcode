class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        number_dict = {}
        for i in range(len(nums)):
            number_dict[nums[i]] = i

        for j in range(len(nums)):
            complement = target - nums[j]
            if complement in number_dict.keys():
                if j == number_dict[complement]:
                    continue
                result.append(j)
                result.append(number_dict[complement])
                return result
