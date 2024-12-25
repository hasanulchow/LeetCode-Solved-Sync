class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculates the number of distinct ways to climb to the top of a staircase with n steps.
        You can climb either 1 step or 2 steps at a time.

        Args:
        n (int): The total number of steps.

        Returns:
        int: The number of ways to reach the top.
        """
        # Initialize a memoization dictionary to store previously calculated results
        memo = {}
        # Call the helper function with the total number of steps and the memo dictionary
        return self.helper(n, memo)
    
    def helper(self, n: int, memo: dict[int, int]) -> int:
        """
        Recursive helper function with memoization to calculate the number of ways to climb stairs.

        Args:
        n (int): The number of steps left to climb.
        memo (dict): A dictionary to store previously computed results for subproblems.

        Returns:
        int: The number of ways to climb the remaining steps.
        """
        # Base cases: If there are 0 or 1 steps, there is only 1 way to climb
        if n == 0 or n == 1:
            return 1
        
        # Check if the result for the current number of steps is already in the memo
        if n not in memo:
            # Compute the result recursively:
            # Ways to climb n steps = ways to climb (n-1) steps + ways to climb (n-2) steps
            memo[n] = self.helper(n - 1, memo) + self.helper(n - 2, memo)
        
        # Return the stored result
        return memo[n]
