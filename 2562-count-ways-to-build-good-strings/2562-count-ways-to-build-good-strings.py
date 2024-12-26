class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high+1)
        dp[0] = 1
        ans = 0
        for i in range(1, high+1):
            dp[i] = ((dp[i-zero] if i-zero>=0 else 0) + (dp[i-one] if i-one>=0 else 0)) % 1000000007
            if i >= low:
                ans = (ans + dp[i]) % 1000000007
        return ans