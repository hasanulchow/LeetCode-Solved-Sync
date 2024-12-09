class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Initialize a 2D list (matrix) to store the length of the longest common subsequence (LCS)
        l = [[0 for i in range(len(t) + 1)] for j in range(len(s) + 1)]
        
        # Build the LCS matrix
        for i in range(len(s)):
            for j in range(len(t)):
                # If characters match, increment the subsequence length
                if s[i] == t[j]:
                    l[i + 1][j + 1] = l[i][j] + 1
                # Otherwise, take the maximum subsequence length from previous computations
                else:
                    l[i + 1][j + 1] = max(l[i][j + 1], l[i + 1][j])
        
        # If the length of the subsequence of 's' matches the LCS length at the bottom-right corner, return True
        if len(s) == l[len(s)][len(t)]:
            return True
        else:
            return False
