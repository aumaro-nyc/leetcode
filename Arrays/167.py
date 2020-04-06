class Solution:
    """
    Time: 13% (92ms)
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        result = []
        while low < high:
            total = numbers[low] + numbers[high]
            if total == target:
                result.append(low+1)
                result.append(high+1)
                return result
            elif total > target:
                high -= 1
            else:
                low += 1
