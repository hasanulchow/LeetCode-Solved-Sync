class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotates the input n x n 2D matrix 90 degrees clockwise in-place.
        """
        edge_length = len(matrix)

        # Step 1: Reverse the rows of the matrix (flip vertically).
        top = 0
        bottom = edge_length - 1
        while top < bottom:
            for col in range(edge_length):
                # Swap elements from the top and bottom rows.
                temp = matrix[top][col]
                matrix[top][col] = matrix[bottom][col]
                matrix[bottom][col] = temp

            top += 1
            bottom -= 1

        # Step 2: Transpose the matrix (swap rows and columns).
        for row in range(edge_length):
            for col in range(row + 1, edge_length):
                # Swap elements at (row, col) and (col, row).
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp

        # No need to return the matrix as it is modified in place.
