from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()  # Set to track visited cells
        rows, cols = len(grid), len(grid[0])  # Get the dimensions of the grid

        # Helper function to perform BFS starting from the cell (r, c)
        def bfs(r, c):
            q = deque()  # Queue for BFS
            visited.add((r, c))  # Mark the starting cell as visited
            q.append((r, c))  # Add the starting cell to the queue

            while q:
                row, col = q.popleft()  # Pop the first element from the queue
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # Directions: down, up, right, left

                # Explore all the four possible directions from the current cell
                for dr, dc in directions:
                    r, c = row + dr, col + dc  # Compute new position

                    # Check if the new position is within bounds, is a land cell ("1"), and has not been visited
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r, c) not in visited:
                        q.append((r, c))  # Add the new cell to the queue
                        visited.add((r, c))  # Mark the new cell as visited

        # Traverse through every cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1  # Found a new island, increment the island count
                    bfs(r, c)  # Perform BFS to mark the entire island as visited

        return islands  # Return the total number of islands
