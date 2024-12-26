class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for i in range(len(s))] for j in range(len(s))]

        for width in range(1,len(s)+1):
            for i in range(len(s)-width+1):
                j = i+width-1
                #i is the start index of the substring
                #j is the end index of the substring
                #width is the length of the substring
                if width == 1:
                    dp[i][j] = 1
                elif width == 2:
                    if s[i] == s[j]:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 1
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1] + 2
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][len(s)-1]
   