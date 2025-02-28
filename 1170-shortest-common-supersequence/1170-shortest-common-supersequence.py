class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        M = len(str1)
        N = len(str2)

        dp = [[0]*(N+1) for _ in range(M+1)]
        for i in range(M):
            for j in range(N):
                if str1[i]==str2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        i = M
        j = N
        ans = ""
        while i>0 and j>0:
            if str1[i-1]==str2[j-1]:
                ans = str1[i-1]+ans
                i-=1
                j-=1
            else:
                if dp[i-1][j]==dp[i][j]:
                    ans = str1[i-1]+ans
                    i-=1
                else:
                    ans = str2[j-1]+ans
                    j-=1

        while i>0:
            ans = str1[i-1]+ans
            i-=1

        while j>0:
            ans = str2[j-1]+ans
            j-=1
        return ans