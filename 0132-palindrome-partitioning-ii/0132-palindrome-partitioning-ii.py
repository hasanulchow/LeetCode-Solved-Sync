class Solution:
    def minCut(self, S: str) -> int:
        N = len(S)
        
        # dp[i] will hold the minimum cuts needed for the substring S[0:i]
        dp = [-1] + [N] * N  # Initialize with N as the maximum possible cuts
        
        # Expand palindromes and update dp array
        for i in range(2 * N - 1):
            # Determine left and right bounds of the potential palindrome center
            l = i // 2
            r = l + (i & 1)  # if i is even, r = l, if odd, r = l + 1
            
            # Check the palindrome around the current center (l, r)
            while 0 <= l and r < N and S[l] == S[r]:
                dp[r + 1] = min(dp[r + 1], dp[l] + 1)  # Update the cuts needed
                l -= 1  # Expand left pointer
                r += 1  # Expand right pointer
        
        return dp[-1]  # The result is the number of cuts for the entire string
