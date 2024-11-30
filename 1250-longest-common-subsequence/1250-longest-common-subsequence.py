class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        
        # Initialize the dp array with dimensions (n+1) x (m+1)
        dp = [[-1] * (m+1) for _ in range(n+1)]
        
        def lcs(i, j):
            # Base case: if one of the strings is empty
            if i == n or j == m:
                return 0
            
            # Check if we have already computed the result for this pair (i, j)
            if dp[i][j] != -1:
                return dp[i][j]
            
            # If characters match, the LCS includes this character
            if text1[i] == text2[j]:
                dp[i][j] = 1 + lcs(i + 1, j + 1)
            else:
                # Otherwise, we take the maximum LCS by either excluding the current character from text1 or text2
                dp[i][j] = max(lcs(i + 1, j), lcs(i, j + 1))
            
            return dp[i][j]
        
        return lcs(0, 0)
