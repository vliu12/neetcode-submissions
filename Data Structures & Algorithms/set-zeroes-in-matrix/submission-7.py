class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        rows, cols = [False] * ROWS, [False] * COLS


        for row in range(ROWS):
            for col in range(COLS):
                if (matrix[row][col] == 0):
                    rows[row] = True
                    cols[col] = True

        for r in range(ROWS):
            for c in range(COLS):
                if rows[r] or cols[c]:
                    matrix[r][c] =0
                    
                    

        
        