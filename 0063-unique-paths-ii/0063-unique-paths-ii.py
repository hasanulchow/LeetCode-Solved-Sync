class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        Calculates the number of unique paths in a grid from the top-left corner to the bottom-right corner,
        where some cells contain obstacles, represented by 1s. You can only move right or down.

        Args:
        obstacleGrid (List[List[int]]): A 2D grid representing the obstacle positions.
            0 represents an open cell, and 1 represents an obstacle.

        Returns:
        int: The number of unique paths from the top-left to the bottom-right corner.
        """
        # Check if the starting cell is blocked or the grid is empty
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
            return 0  # No valid path if the start is blocked or grid is empty
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])  # m = number of rows, n = number of columns
        
        # Initialize two arrays to store the number of paths for the current and previous rows
        previous = [0] * n
        current = [0] * n
        previous[0] = 1  # There's one way to start (from the top-left corner)
        
        for i in range(m):
            # Handle the first column separately: 0 if there's an obstacle, else inherit from previous row
            current[0] = 0 if obstacleGrid[i][0] == 1 else previous[0]
            
            for j in range(1, n):
                # If the current cell is an obstacle, set current[j] to 0
                # Otherwise, sum the paths from the left and top cells (current[j-1] and previous[j])
                current[j] = 0 if obstacleGrid[i][j] == 1 else current[j-1] + previous[j]
            
            # Move to the next row by copying the current row to previous row
            previous[:] = current
        
        # The answer is in the bottom-right corner (previous[n-1] after the last iteration)
        return previous[n-1]
