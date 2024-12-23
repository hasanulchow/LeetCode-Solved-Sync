class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        This function calculates the number of distinct subsequences of string `s` that match string `t`.

        We use Dynamic Programming (DP) to solve this problem efficiently.

        Approach:
        1. Initialize a DP table `dp` where `dp[i][j]` represents the number of distinct subsequences of the first `i` characters of `s` that match the first `j` characters of `t`.
        2. The base case is that for any `i`, `dp[i][0]` is 1, meaning an empty string `t` can always be formed by any subsequence of `s`.
        3. For each character of `s` and `t`, we have two choices:
           - Exclude the current character of `s`, in which case `dp[i][j] = dp[i-1][j]`.
           - Include the current character of `s` if it matches the current character of `t`, in which case `dp[i][j] += dp[i-1][j-1]`.
        4. Finally, `dp[m][n]` will give the number of distinct subsequences of `s` that match `t`.

        Time Complexity: O(m * n), where `m` is the length of `s` and `n` is the length of `t`. We fill a DP table of size `(m+1) x (n+1)`.
        Space Complexity: O(m * n) for the DP table.
        """
        
        m, n = len(s), len(t)

        # Create a DP table with dimensions (m+1) x (n+1), initialized to 0
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        # Base case: an empty string `t` can always be formed from any subsequence of `s`
        for i in range(m+1):
            dp[i][0] = 1
        
        # Fill the DP table
        for i in range(1, m+1):  # Iterate over each character in `s`
            for j in range(1, n+1):  # Iterate over each character in `t`
                dp[i][j] = dp[i-1][j]  # Case 1: Exclude the current character of `s`
                if s[i-1] == t[j-1]:  # Case 2: Include the current character of `s`
                    dp[i][j] += dp[i-1][j-1]
        
        # The final answer is stored in dp[m][n]
        return dp[m][n]
