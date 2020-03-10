class Solution:
    """
    Time: 70% (124ms)
    """
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = -1
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > current_max:
                arr[i], current_max = current_max, arr[i]
            else:
                arr[i] = current_max
        return arr
