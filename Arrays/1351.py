class Solution:
    """
    Cleaner solution, but *MARGINALLY* slower
    Time: 87%-93% (120ms)
    """
    def countNegatives(self, grid: List[List[int]]) -> int:
        length = len(grid[0])
        count = 0
        for row in grid:
            for i in range(0,length):
                if row[i] < 0:
                    count += length - i
                    break
        return count

class Solution:
    """
    Faster due to adding row*column negative counts instead of 1 single line at a time
    Time: 93%-98% (116ms)g
    """
    def countNegatives(self, grid: List[List[int]]) -> int:
        check_len = len(grid[0])
        length = len(grid)
        total = 0

        for i in range(length):
            if grid[i][0] < 0:
                total += ((length - i) * (check_len))
                break
            for j in range(check_len):
                if grid[i][j] < 0:
                    total += ((length - i) * (check_len - j))
                    check_len = j
                    break
        return total
