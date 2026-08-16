class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # not number of groups, but number of elems in the largest group
        
        # dfs
        rows = len(grid)
        cols = len(grid[0])
        curr_size = 0

        def dfs(i, j):
            nonlocal curr_size
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return 

            if grid[i][j] == 0:
                return

            grid[i][j] = 0

            curr_size += 1

            dfs(i, j-1)
            dfs(i-1,j)
            dfs(i+1, j)
            dfs(i, j + 1)


        best = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    dfs(row, col)
                    best = max(curr_size, best)
                    curr_size = 0

        return best


        


