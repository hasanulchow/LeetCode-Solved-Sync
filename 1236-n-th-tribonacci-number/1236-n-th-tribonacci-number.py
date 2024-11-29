class Solution:
    def tribonacci(self, n: int) -> int:
        # Memoization function with dp array passed
        def memo(n, dp):
            # Base case for n = 0, 1, 2
            if n <= 2:
                return dp[n]
            
            # If the value is already computed, return it from dp
            if dp[n] != -1:
                return dp[n]
            
            # Recursive calculation for tribonacci number
            dp[n] = memo(n - 1, dp) + memo(n - 2, dp) + memo(n - 3, dp)
            
            return dp[n]
        
        # Handle base cases where n = 0, 1, 2 directly
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        # Initialize dp array with -1, and base cases for dp[0], dp[1], dp[2]
        dp = [-1] * (n + 1)
        dp[0], dp[1], dp[2] = 0, 1, 1
        
        # Call the memoization function to compute the tribonacci value for n
        return memo(n, dp)
