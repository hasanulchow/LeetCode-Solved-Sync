class Solution(object):
    def minimumTotal(self, triangle):
        """
        Finds the minimum path sum from the top to the bottom of a triangle.

        Args:
        triangle (List[List[int]]): A 2D list representing the triangle.

        Returns:
        int: The minimum path sum from the top to the bottom.
        """
        n = len(triangle)  # Get the number of rows in the triangle.

        # Start from the second last row and move upwards.
        for i in range(n - 2, -1, -1):  # Iterate from the second last row to the top row.
            for j in range(len(triangle[i])):  # Iterate through each element in the current row.
                # Find the minimum of the two adjacent numbers in the row directly below.
                min_sum = min(triangle[i + 1][j], triangle[i + 1][j + 1])
                current_val = triangle[i][j]  # The current value in the triangle at position (i, j).
                triangle[i][j] = current_val + min_sum  # Update the current position with the minimum sum.

        return triangle[0][0]  # The top element of the triangle now contains the minimum total.
