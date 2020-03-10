class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        count = 0
        row_count = [0] * n
        col_count = [0] * m

        for ind in indices:
            row_count[ind[0]] += 1
            col_count[ind[1]] += 1

        for i in range(n):
            for j in range(m):
                count += 1 if (row_count[i] + col_count[j]) % 2 != 0 else 0
        return count
