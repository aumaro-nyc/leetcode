class Solution:
    """
    Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all
    elements in arr2 are also in arr1.

    Sort the elements of arr1 such that the relative ordering of items in arr1
    are the same as in arr2.  Elements that don't appear in arr2 should be
    placed at the end of arr1 in ascending order.

    Time: 99% (24ms)
    """
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        freq_map = {}
        for n in arr1:
            if n not in freq_map:
                freq_map[n] = 1
            else:
                freq_map[n] += 1
        for n in arr2:
            result += [n] * freq_map[n]
            del freq_map[n]
        for item in sorted(freq_map):
            result += [item] * freq_map[item]
        return result
