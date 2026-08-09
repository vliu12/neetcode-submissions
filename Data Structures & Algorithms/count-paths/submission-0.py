class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dp (i, j):
            if i == n-1 and j == m - 1: 
                a = 1
            elif i == n - 1:
                a = dp (i, j + 1)
            elif j == m - 1:
                a = dp (i + 1, j)
            else:
                a = dp (i + 1, j) + dp (i, j + 1)
            return a
        return dp (0, 0)