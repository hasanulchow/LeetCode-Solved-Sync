class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solves the Sudoku puzzle in-place using backtracking and set-based optimization.
        """
        spots = []  # List to store the positions of empty spots
        row = [set() for _ in range(9)]  # Sets to track numbers in each row
        col = [set() for _ in range(9)]  # Sets to track numbers in each column
        sub = [set() for _ in range(9)]  # Sets to track numbers in each 3x3 sub-grid

        # Initialize the sets and identify empty spots
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spots.append((i, j))  # Save empty spot positions
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    sub[i // 3 * 3 + j // 3].add(board[i][j])  # Map to appropriate sub-grid

        # Helper function for backtracking
        def fn(k):
            """Attempts to fill the kth empty spot and returns True if successful."""
            if k == len(spots):  # All spots filled successfully
                return True
            i, j = spots[k]  # Get the row and column of the current spot
            for n in map(str, range(1, 10)):  # Try numbers 1 to 9
                if n not in row[i] and n not in col[j] and n not in sub[i // 3 * 3 + j // 3]:
                    # Place number if valid
                    board[i][j] = n
                    row[i].add(n)
                    col[j].add(n)
                    sub[i // 3 * 3 + j // 3].add(n)

                    if fn(k + 1):  # Recursively fill the next spot
                        return True

                    # Backtrack: Remove the number and try the next option
                    board[i][j] = "."
                    row[i].remove(n)
                    col[j].remove(n)
                    sub[i // 3 * 3 + j // 3].remove(n)
            return False

        # Start solving from the first empty spot
        fn(0)
