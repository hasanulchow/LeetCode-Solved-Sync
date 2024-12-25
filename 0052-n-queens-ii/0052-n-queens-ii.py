class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        Returns the number of distinct solutions to the N-Queens problem for a given board size.

        Args:
        n (int): The size of the chessboard (n x n).

        Returns:
        int: The number of distinct solutions.
        """
        # Initialize variables
        res = 0  # To store the number of valid solutions
        col = set()  # Columns that are already attacked by queens
        pos = set()  # Positive diagonals that are attacked (r + c)
        neg = set()  # Negative diagonals that are attacked (r - c)

        def backtracking(r):
            """
            Recursive function to place queens row by row.
            
            Args:
            r (int): The current row being processed.
            """
            # Base case: all queens are placed successfully
            if n == r:
                nonlocal res
                res += 1
                return

            # Try placing a queen in each column of the current row
            for c in range(n):
                # Skip the column if it's already attacked by another queen
                if c in col or (c + r) in pos or (r - c) in neg:
                    continue

                # Place the queen and mark the column and diagonals as attacked
                col.add(c)
                pos.add(c + r)
                neg.add(r - c)

                # Move to the next row
                backtracking(r + 1)

                # Backtrack: remove the queen and unmark the column and diagonals
                col.remove(c)
                pos.remove(c + r)
                neg.remove(r - c)

        # Start backtracking from the first row
        backtracking(0)

        return res
