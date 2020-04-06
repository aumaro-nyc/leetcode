class Solution:
    """
    Time: 25% (52ms)
    """
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        result = [[1]]
        for i in range(2, numRows +  1):
            new_row = [1] * i
            prev_row = result[i - 2]
            for j in range(1,len(new_row) - 1):
                new_row[j] = prev_row[j-1] + prev_row[j]
            result.append(new_row)
        return result
