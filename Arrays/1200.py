class Solution:
    """
    Given an array of distinct integers arr, find all pairs of elements with
    the minimum absolute difference of any two elements. 

    Time: 53% (372ms) O(nlogn) -> built in sort
    """
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        result = []
        arr.sort()
        min_diff = float('inf')
        i,j = 0,1

        while j < len(arr):
            diff = arr[j] - arr[i]
            if diff < min_diff:
                min_diff = diff
                result = [[arr[i],arr[j]]]
            elif diff == min_diff:
                result.append([arr[i],arr[j]])
            i += 1
            j += 1
        return result
