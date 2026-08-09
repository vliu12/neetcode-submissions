from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    # check bounds + land + not visited
                    if (0 <= nr < rows and 0 <= nc < cols and
                        grid[nr][nc] == "1" and (nr, nc) not in visited):
                        
                        visited.add((nr, nc))
                        q.append((nr, nc))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1

        return islands
