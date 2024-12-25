class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        # dp(i, j, k) := max score of boxes[i..j] if k boxes equal to boxes[j]
        @lru_cache(None)
        def dp(i: int, j: int, k: int) -> int:
            if i > j:
                return 0

            # Check if we can reduce the sub-problem size
            while i < j and boxes[j] == boxes[j-1]:
                j -= 1
                k += 1

            # If we have processed all the boxes, return the score
            if i == j:
                return (k+1)**2

            # Case 1: Remove the last k+1 boxes and recurse on the remaining sub-problem
            ans = (k+1)**2 + dp(i, j-1, 0)

            # Case 2: Merge boxes[j] with some box in the subarray i to j-1 and recurse on the two resulting sub-problems
            for m in range(j-1, i-1, -1):
                if boxes[m] == boxes[j]:
                    ans = max(ans, dp(i, m, k+1) + dp(m+1, j-1, 0))

            return ans

        return dp(0, len(boxes)-1, 0)