class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: If the number of rows is 1 or equal to the length of the string,
        # no zigzag transformation is needed; return the string as is
        if numRows == len(s) or numRows == 1:
            return s

        # Step 1: Initialize the rows for zigzag storage
        rows = ['' for _ in range(numRows)]  # Create a list with `numRows` empty strings
        rowno = 0  # Start at the first row
        dirc = -1  # Direction indicator (-1 for upward, +1 for downward)

        # Step 2: Iterate through the string and fill the rows in a zigzag pattern
        for i in range(len(s)):
            # Reverse direction at the top or bottom of the zigzag
            if rowno == (numRows - 1) or rowno == 0:
                dirc *= -1  # Flip the direction

            # Append the current character to the appropriate row
            rows[rowno] += s[i]

            # Move to the next row based on the current direction
            rowno += dirc

        # Step 3: Combine all rows into the final zigzag string
        return ''.join(rows)  # Concatenate all rows to form the result
