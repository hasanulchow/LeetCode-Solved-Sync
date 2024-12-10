class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Returns all elements of the matrix in spiral order.

        Args:
        matrix (List[List[int]]): The input 2D matrix.

        Returns:
        List[int]: The elements in spiral order.
        """
        result = []
        while matrix:
            # Add the first row to the result
            result += matrix.pop(0)

            # Add the last element of each remaining row
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())

            # Add the last row in reverse order
            if matrix:
                result += matrix.pop()[::-1]

            # Add the first element of each remaining row in reverse order
            if matrix and matrix[0]:
                for row in reversed(matrix):
                    result.append(row.pop(0))

        return result
