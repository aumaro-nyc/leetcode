class Solution:
    """
    Given an integer n, return any array containing n unique integers such that they add up to 0.
    """
    def sumZero(self, n: int) -> List[int]:
        result = []
        for i in range(1,(n // 2) + 1):
            result.append(i)
            result.append(i * -1)
        if n % 2 != 0:
            result.append(0)
        return result
