class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Get the number of rows and columns
        ROWS, COLS = len(board), len(board[0])

        # Define the four possible directions for exploring neighbors (down, up, right, left)
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Depth-first search to mark 'O's connected to the border as 'D'
        def dfs_explore(r, c):
            # If the current cell is out of bounds or not an 'O', stop the search
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                board[r][c] != 'O'):
                return 
            
            # Mark the current 'O' as 'D' to indicate it is not surrounded
            board[r][c] = 'D'

            # Explore the neighboring cells (down, up, right, left)
            for dr, dc in DIRECTIONS:
                dfs_explore(r + dr, c + dc)

        # Step 1: Mark all 'O's connected to the borders (unsurrounded regions)
        # Explore all 'O's on the left and right borders
        for r in range(ROWS):
            if board[r][0] == 'O':  
                dfs_explore(r, 0)  # Explore from the left border
            if board[r][COLS - 1] == 'O':  
                dfs_explore(r, COLS - 1)  # Explore from the right border

        # Explore all 'O's on the top and bottom borders
        for c in range(COLS):
            if board[0][c] == 'O':  
                dfs_explore(0, c)  # Explore from the top border
            if board[ROWS - 1][c] == 'O':  
                dfs_explore(ROWS - 1, c)  # Explore from the bottom border

        # Step 2: Capture surrounded regions (flip 'O' to 'X') and restore borders (flip 'D' back to 'O')
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O':
                    board[row][col] = 'X'  # Flip 'O' to 'X' because it is surrounded

                elif board[row][col] == 'D':
                    board[row][col] = 'O'  # Restore 'D' to 'O' because it is connected to the border

    # Time complexity: O(m * n), where m is the number of rows and n is the number of columns
    # Space complexity: O(m * n), due to the recursion stack used by DFS
