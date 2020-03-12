class Solution:
    """
    Given an array of integers A, return the largest integer that only occurs once.
    If no integer occurs once, return -1.

    Time: 93% (40ms)
    """
    def largestUniqueNumber(self, A: List[int]) -> int:
        number_map = {}
        rejects = {}
        for n in A:
            if n not in number_map and n not in rejects:
                number_map[n] = 1
            else:
                if n in rejects:
                    continue
                else:
                    rejects[n] = 1
                    del number_map[n]
        maximum = max(number_map) if len(number_map) > 0 else -1
        return maximum
