class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        
        # Initialize dp array for previous row and current row
        dp = [i for i in range(l2 + 1)]
        c = [0 for _ in range(l2 + 1)]
        
        # Iterate through each character of word1
        for i in range(1, l1 + 1):
            c[0] = i  # Initialize the first column for current row
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:  # If characters match
                    c[j] = dp[j - 1]  # No operation needed, carry over the previous value
                else:
                    c[j] = 1 + min(dp[j], dp[j - 1], c[j - 1])  # Calculate min operation
            dp = c.copy()  # Copy the current row to dp (previous row for next iteration)

        return dp[-1]  # The last element of dp is the result
