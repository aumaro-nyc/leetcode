class Solution:
    """
    Time: 54% (112ms)
    """
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for ele1 in arr1:
            valid = True
            for ele2 in arr2:
                if abs(ele1 - ele2) <= d:
                    valid = False
                    break
            count += 1 if valid else 0
        return count
