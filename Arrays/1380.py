class Solution:
    """
    Given a m * n matrix of distinct numbers, return all lucky numbers in
    the matrix in any order.

    A lucky number is an element of the matrix such that it is the minimum
    element in its row and maximum in its column.

    Time: 93% (132ms)
    """
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        result = []
        col_max = [0] * len(matrix[0])
        for j in range(len(matrix[0])):
            current_max = float('-inf')
            row = 0
            for i in range(len(matrix)):
                if matrix[i][j] > current_max:
                    current_max = matrix[i][j]
                    row = i
            if current_max == min(matrix[row]):
                result.append(current_max)
        return result
