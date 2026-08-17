from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        land = 2147483647

        rows = len(grid)
        cols = len(grid[0])

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
        
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

            
        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and grid[nr][nc] == land
                ):

                    grid[nr][nc] = grid[row][col] + 1
                    queue.append((nr, nc))
