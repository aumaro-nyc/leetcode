from collections import deque
class Solution:
    """
    Time: 61% (104ms)
    """
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(nums) * len(nums[0]):
            return nums
        else:
            if r == len(nums) and c == len(nums[0]):
                return nums
            else:
                result = []
                choices = deque()
                for row in nums:
                    for item in row:
                        choices.append(item)
                for i in range(r):
                    row = []
                    for j in range(c):
                        row.append(choices.popleft())
                    result.append(row)
                return result
