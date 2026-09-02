class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or r >= rows or c >= cols or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False

            original = board[r][c]
            board[r][c] = '#'

            res = False

            for (dr, dc) in dirs:
                nr = r + dr
                nc = c + dc

                # from this position, can we finish the word
                res = res or dfs(nr, nc, i + 1) 

            board[r][c] = original
            
            return res



        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False



