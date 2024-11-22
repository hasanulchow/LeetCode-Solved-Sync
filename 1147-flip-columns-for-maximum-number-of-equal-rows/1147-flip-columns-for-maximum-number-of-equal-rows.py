class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_count = {}  # Dictionary to store the frequency of row patterns

        for row in matrix:
            # Normalize the row: flip it if the first element is 1, otherwise keep it as is
            normalized = tuple(cell if row[0] == 0 else 1 - cell for cell in row)

            # Count the occurrence of each normalized row pattern
            if normalized not in pattern_count:
                pattern_count[normalized] = 0
            pattern_count[normalized] += 1

        # Return the maximum frequency of any row pattern (after flips)
        return max(pattern_count.values())
