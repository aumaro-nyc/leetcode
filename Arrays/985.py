class Solution:
    """
    Time: 72% (552ms)
    """
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        total = 0
        for element in A:
            total += element if element % 2 == 0 else 0
        for q in queries:
            total -= A[q[1]] if A[q[1]] % 2 == 0 else 0
            A[q[1]] += q[0]
            total += A[q[1]] if A[q[1]] % 2 == 0 else 0
            result.append(total)
        return result
