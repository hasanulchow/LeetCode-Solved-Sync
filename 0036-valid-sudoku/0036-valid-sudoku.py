from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Validates if a given 9x9 Sudoku board is valid.

        Args:
        board (List[List[str]]): The 9x9 Sudoku board.

        Returns:
        bool: True if the board is valid, False otherwise.
        """
        rows = defaultdict(set)  # To track numbers in each row
        cols = defaultdict(set)  # To track numbers in each column
        boxes = defaultdict(set)  # To track numbers in each 3x3 sub-box

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                # Check for duplicates in row, column, or box
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in boxes[(r // 3, c // 3)]
                ):
                    return False  # Duplicate found, invalid Sudoku

                # Add the number to the respective row, column, and box
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])

        return True  # If no duplicates are found, the board is valid
