class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*101 for i in range(101)]
        def count(r,c):
            if r == 1 or c == 1:
                return 1
            if dp[r][c]:
                return dp[r][c]
            left = count(r-1,c)
            right = count(r,c-1)
            dp[r][c] = left + right
            return dp[r][c]

        return count(m,n)
        