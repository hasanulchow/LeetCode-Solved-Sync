class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        Solve the Snakes and Ladders game using a BFS approach.
        :param board: List[List[int]] - A 2D list representing the board
        :return: int - The minimum number of moves to reach the final square, or -1 if it's impossible
        """
        n = len(board)  # The board is n x n

        # Helper function to convert a board label to a board position (row, column)
        def label_to_position(label):
            r, c = divmod(label - 1, n)  # Determine row and column (0-indexed)
            # Reverse the row ordering (board starts at bottom row)
            row = n - 1 - r
            # Determine column direction based on row parity
            col = c if r % 2 == 0 else n - 1 - c
            return row, col

        # Set to keep track of visited labels (to avoid revisiting)
        seen = set()

        # BFS queue: stores tuples of (label, step_count)
        queue = collections.deque()
        queue.append((1, 0))  # Start at label 1 with 0 moves

        # BFS traversal
        while queue:
            label, step = queue.popleft()  # Get the current position and step count
            r, c = label_to_position(label)  # Get the board position for the label

            # Check if there's a snake or ladder at the current position
            if board[r][c] != -1:
                label = board[r][c]  # Move to the destination of the snake/ladder

            # Check if we've reached the last square
            if label == n * n:
                return step

            # Roll the dice (1 to 6)
            for x in range(1, 7):
                new_label = label + x  # Calculate the next label
                if new_label <= n * n and new_label not in seen:  # Check bounds and avoid revisiting
                    seen.add(new_label)  # Mark the new label as visited
                    queue.append((new_label, step + 1))  # Add to the queue with incremented step count

        # If we exhaust the queue without reaching the last square, return -1
        return -1
