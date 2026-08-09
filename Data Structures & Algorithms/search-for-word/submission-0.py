class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        path = set()
        rows = len(board)
        cols = len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or r >= rows or c >= cols or
                word[i] != board[r][c] or (r, c) in path):
                return False

            path.add((r, c))
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, i + 1):
                    path.remove((r, c))
                    return True

            path.remove((r, c))
            
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False

        




                    