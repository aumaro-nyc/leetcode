class Solution:
    """
    Time: 78% (508ms)
    """
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) == 1: return True
        i = 1
        last = A[0]
        while A[0] == A[i]:
            if i == len(A) - 1:
                return True
            last = A[i]
            i += 1
        ascending = True if last < A[i] else False
        while i < len(A):
            if ascending:
                if A[i] < last:
                    return False
                else:
                    last = A[i]
                    i += 1
                    continue
            if not ascending:
                if A[i] > last:
                    return False
                else:
                    last = A[i]
                    i += 1
                    continue
        return True
