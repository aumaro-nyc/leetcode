class Solution:
    """
    A matrix is Toeplitz if every diagonal from top-left to bottom-right has
    the same element.

    Now given an M x N matrix, return True if and only if the matrix is
    Toeplitz.

    Time: 64% (88ms)
    """
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        i = 0
        j = 0
        while j < len(matrix[0]):
            element = matrix[i][j]
            diag_i = 0
            diag_j = j
            while diag_i < len(matrix) and diag_j < len(matrix[0]):
                if matrix[diag_i][diag_j] != element:
                    return False
                diag_i += 1
                diag_j += 1
            j += 1

        i = len(matrix) - 1
        j = 0
        while i > 0:
            element = matrix[i][j]
            diag_i = i
            diag_j = 0
            while diag_i < len(matrix) and diag_j < len(matrix[0]):
                if matrix[diag_i][diag_j] != element:
                    return False
                diag_i += 1
                diag_j += 1
            i -= 1
        return True
