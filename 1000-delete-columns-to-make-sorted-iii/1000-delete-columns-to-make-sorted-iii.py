class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                valid = True
                for a in strs:
                    if a[j] > a[i]: 
                        valid = False
                        break
                if valid:
                    dp[i] = max(dp[i], dp[j] + 1)
        return n - max(dp)