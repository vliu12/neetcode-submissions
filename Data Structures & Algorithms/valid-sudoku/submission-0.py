class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def checkRow(board, row):
            seen = set()

            for col in range(9):
                val = board[row][col]

                if val == ".":
                    continue

                if val in seen:
                    return False

                seen.add(val)

            return True

        def checkCol(board, col):
            seen = set()

            for row in range(9):
                val = board[row][col]

                if val == ".":
                    continue

                if val in seen:
                    return False

                seen.add(val)

            return True

        def check3x3(board, start_row, start_col):
            seen = set()

            for i in range(3):
                for j in range(3):
                    val = board[start_row + i][start_col + j]

                    if val == ".":
                        continue

                    if val in seen:
                        return False

                    seen.add(val)

            return True

        # Check every row and column
        for idx in range(9):
            if not checkRow(board, idx):
                return False

            if not checkCol(board, idx):
                return False

        # Check every 3x3 box
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not check3x3(board, i, j):
                    return False

        return True