class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        ans = 1
        for item in arr:
            val = 1
            if item - difference in dp:
                val += dp[item-difference]
                ans = max(ans, val)
            dp[item] = val
        
        return ans
        