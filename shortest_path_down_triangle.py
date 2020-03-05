class Solution:
    """
    Slow when processing very large inputs
    Passes 42/43 test cases, but needs DP to be efficient
    """
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        def dfs(i, j, triangle):
            if 0 <= i < len(triangle) and 0 <= j < len(triangle[i]):
                if i == len(triangle) - 1:
                    return triangle[i][j]
                else:
                    left = dfs(i+1,j,triangle)
                    right = dfs(i+1,j+1,triangle)
                    return triangle[i][j] + min(left,right)

            else:
                return float('inf')

        return dfs(0,0,triangle)
