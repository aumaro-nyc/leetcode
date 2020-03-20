class Solution:
    """
    Time: 60% (90ms)
    """
    def findSpecialInteger(self, arr: List[int]) -> int:
        target = len(arr) // 4
        current = arr[0]
        if len(arr) == 1: return current
        i = 1
        while i < len(arr):
            if arr[i + target] == current:
                return current
            else:
                while arr[i] == current:
                    i += 1
                current = arr[i]
