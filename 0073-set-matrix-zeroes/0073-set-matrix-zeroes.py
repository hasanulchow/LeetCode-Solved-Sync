class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Modifies the input matrix in-place such that if any cell is 0,
        its entire row and column are set to 0.
        """
        # Get the number of rows in the matrix
        rows = len(matrix)
        # Get the number of columns in the matrix
        cols = len(matrix[0])

        # Initialize a flag to check if the first row has any zero
        first_row_has_zero = False        
        # Initialize a flag to check if the first column has any zero
        first_col_has_zero = False

        # Check if the first row contains any zero
        for c in range(cols):  # Iterate over all columns in the first row
            if matrix[0][c] == 0:  # If a zero is found in the first row
                first_row_has_zero = True  # Set the flag to True
                break  # No need to check further

        # Check if the first column contains any zero
        for r in range(rows):  # Iterate over all rows in the first column
            if matrix[r][0] == 0:  # If a zero is found in the first column
                first_col_has_zero = True  # Set the flag to True
                break  # No need to check further
        
        # Use the first row and column as markers for other rows and columns
        for r in range(1, rows):  # Start from the second row
            for c in range(1, cols):  # Start from the second column
                if matrix[r][c] == 0:  # If the current cell is zero
                    matrix[r][0] = 0  # Mark the first cell of the row
                    matrix[0][c] = 0  # Mark the first cell of the column
        
        # Set cells to zero based on the markers in the first row
        for r in range(1, rows):  # Iterate over all rows starting from the second
            if matrix[r][0] == 0:  # If the row is marked
                for c in range(1, cols):  # Iterate over all columns in this row
                    matrix[r][c] = 0  # Set the cell to zero

        # Set cells to zero based on the markers in the first column
        for c in range(1, cols):  # Iterate over all columns starting from the second
            if matrix[0][c] == 0:  # If the column is marked
                for r in range(1, rows):  # Iterate over all rows in this column
                    matrix[r][c] = 0  # Set the cell to zero
    
        # Set the entire first row to zero if the flag is True
        if first_row_has_zero:  # Check if the first row needs to be zeroed
            for c in range(cols):  # Iterate over all columns in the first row
                matrix[0][c] = 0  # Set the cell to zero

        # Set the entire first column to zero if the flag is True
        if first_col_has_zero:  # Check if the first column needs to be zeroed
            for r in range(rows):  # Iterate over all rows in the first column
                matrix[r][0] = 0  # Set the cell to zero
