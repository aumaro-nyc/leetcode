class Solution:
    """
    Given an array A of distinct integers sorted in ascending order,
    return the smallest index i that satisfies A[i] == i.  Return -1 if
    no such i exists.

    Time: 69% (64ms)
    """
    def fixedPoint(self, A: List[int]) -> int:
        for i in range(len(A)):
            if A[i] < 0: continue
            if i == A[i]:
                return i
        return -1
