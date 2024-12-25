class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Finds the minimum path sum from the top-left to the bottom-right corner
        of a grid, moving only down or right at each step.

        Args:
        grid (List[List[int]]): The input grid with non-negative integers.

        Returns:
        int: The minimum path sum.
        """
        # Get the dimensions of the grid (m = number of rows, n = number of columns)
        m, n = len(grid), len(grid[0])

        # Initialize the first column (can only come from above)
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]  # Add the value from the cell above

        # Initialize the first row (can only come from the left)
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]  # Add the value from the cell to the left

        # Fill in the rest of the grid by taking the minimum of the cell above
        # or the cell to the left, then add the current cell's value
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])  # Add the minimum of the top or left cell

        # The value in the bottom-right corner is the minimum path sum
        return grid[-1][-1]  # Return the minimum path sum in the bottom-right corner
    