class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Modify the board in-place to compute the next state in the Game of Life.
        """
        directions = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        
        # Step 1: Mark cells for state changes
        for i in range(len(board)):
            for j in range(len(board[0])):
                live_neighbors = 0
                
                # Count live neighbors
                for x, y in directions:
                    if 0 <= i + x < len(board) and 0 <= j + y < len(board[0]) and abs(board[i + x][j + y]) == 1:
                        live_neighbors += 1
                
                # Apply rules
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = -1  # Live to dead
                if board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 2  # Dead to live

        # Step 2: Update the board to the next state
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 1 if board[i][j] > 0 else 0
