class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #dfs
        numGroups = 0
        rows = len(grid)
        cols = len(grid[0])
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return

            if grid[i][j] == "0":
                return
            
            grid[i][j] = "0"

            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i, j+1)

        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    numGroups += 1
                    dfs(row, col)

        return numGroups