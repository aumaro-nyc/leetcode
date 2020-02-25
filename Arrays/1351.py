class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        length = len(grid[0])
        count = 0
        for row in grid:
            for i in range(0,length):
                if row[i] < 0:
                    count += length - i
                    break
        return count
