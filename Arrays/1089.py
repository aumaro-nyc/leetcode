class Solution:
    """
    Time: 84% (68ms)
    """
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        queue = []
        for i in range(len(arr)):
            if arr[i] == 0:
                queue.append(0)
                queue.append(0)
                arr[i] = queue.pop(0)
            else:
                queue.append(arr[i])
                arr[i] = queue.pop(0)
