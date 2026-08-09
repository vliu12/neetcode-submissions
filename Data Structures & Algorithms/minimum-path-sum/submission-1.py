class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        from functools import lru_cache
        
        @lru_cache(None)
        def dp (i, j): 
            if i == 0 and j == 0:
                a = grid[0][0]
            elif j == 0:
                a = dp(i - 1, j) + grid[i][j]
            elif i == 0:
                a = dp(i, j - 1) + grid[i][j]
            else:
                a = min(dp(i - 1, j), dp(i, j - 1)) + grid[i][j]
            return a
        return dp (n - 1, m - 1)