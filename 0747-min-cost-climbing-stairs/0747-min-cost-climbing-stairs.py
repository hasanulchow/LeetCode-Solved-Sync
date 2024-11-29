from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Memoization dictionary to store the results of subproblems
        memo = {}
        
        def dp(n):
            # If the result for this subproblem has been computed, return it from the memo dictionary
            if n in memo:
                return memo[n]
            
            # Base case: If the step index is less than 2, return the cost at that step
            if n < 2:
                return cost[n]

            # Calculate the cost for this step and store it in the memo dictionary
            memo[n] = cost[n] + min(dp(n-1), dp(n-2))
            return memo[n]
        
        length = len(cost)
        
        # We want the minimum cost to reach the top, which could be either from step n-1 or n-2
        return min(dp(length-1), dp(length-2))
