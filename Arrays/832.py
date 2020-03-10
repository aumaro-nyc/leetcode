class Solution:
    """
    Given a binary matrix A, we want to flip the image horizontally,
    then invert it, and return the resulting image.

    Time: 94% (44ms)
    """
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            i = 0
            j = len(A) - 1
            while i <= j:
                if i == j:
                    row[i] = abs(row[i] - 1)
                else:
                    row[i], row[j] = abs(row[j] - 1), abs(row[i] - 1)
                i += 1
                j -= 1
        return A
