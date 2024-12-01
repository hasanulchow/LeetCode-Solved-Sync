class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        for num in range(n+1):
            dp[num]=dp[int(num/2)]+num%2

        return dp