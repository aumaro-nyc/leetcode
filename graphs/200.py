class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Returns the number of islands present in a 2-dimensional
        matrix. Islands are defined by clusters of "1"s linked
        in one of the four cardinal directions.
        """
        def dfs(grid,row,column):
            """
            Utility function to perform Depth First Search
            starting from first occurence of 1
            """
            if (row >= len(grid) or row < 0) or (column >= len(grid[0]) or column < 0):
                return
            if grid[row][column] == "1":
                grid[row][column] = "-1"
                dfs(grid,row + 1, column)
                dfs(grid,row - 1, column)
                dfs(grid,row, column + 1)
                dfs(grid,row, column - 1)

        count = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == "1":
                    count += 1
                    dfs(grid,row,column)
        return count
