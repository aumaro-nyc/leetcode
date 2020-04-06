class Solution:
    """
    Time: 7% (60ms)
    """
    def transformArray(self, arr: List[int]) -> List[int]:
        changes = True
        while changes:
            changes = False
            prev = arr[0]
            for i in range(1,len(arr) - 1):
                temp = arr[i]
                if prev > arr[i] and arr[i] < arr[i+1]:
                    arr[i] += 1
                    changes = True
                elif prev < arr[i] and arr[i] > arr[i+1]:
                    arr[i] -= 1
                    changes = True
                prev = temp
        return arr
