class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_count = {}

        for row in matrix:
            normalized = tuple(cell if row[0] == 0 else 1 - cell for cell in row)

            if normalized not in pattern_count:
                pattern_count[normalized] = 0

            pattern_count[normalized] += 1


        return max(pattern_count.values())
        