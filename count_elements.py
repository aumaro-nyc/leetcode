class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr.sort()
        i = 0
        repeated = 1
        count = 0
        while i < len(arr) - 1:
            if arr[i] == arr[i+1]:
                repeated += 1
                i += 1
            else:
                count += repeated if abs(arr[i] - arr[i+1]) == 1 else 0
                i += 1
                repeated = 1
        return count
