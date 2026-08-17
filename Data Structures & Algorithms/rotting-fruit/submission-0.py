class Solution:
    from collections import deque

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        time = 0

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        queue = deque()

        time = 0

        fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))

                if grid[row][col] == 1:
                    fresh += 1

        while queue and fresh > 0:

            for i in range(len(queue)):
                    r, c = queue.popleft()

                    for dr, dc in dirs:
                        nr = r + dr
                        nc = c + dc

                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and grid[nr][nc] == 1
                        ):
                            fresh -= 1
                            grid[nr][nc] = 2
                            queue.append((nr, nc))

            # one BFS layer = one minute
            time += 1

        if fresh > 0:
            return -1

        return time


            

                    



