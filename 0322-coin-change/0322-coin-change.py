class Solution(object):
   def coinChange(self, coins, amount):
       """
       :type coins: List[int]
       :type amount: int
       :rtype: int
       """
       # A large value greater than the maximum possible number of coins required
       max_value = amount + 1
       
       # Initialize dp array where dp[i] represents the minimum number of coins needed for amount i
       # dp[i] is initialized with max_value, which is essentially infinity
       dp = [max_value] * (amount + 1)
       
       # Base case: No coins are needed to make the amount 0
       dp[0] = 0
       
       # Iterate through each coin denomination
       for coin in coins:
           # Iterate through all amounts from the current coin value to the target amount
           for x in range(coin, amount + 1):
               # Update dp[x] with the minimum of:
               # 1. The current value of dp[x] (minimum coins needed without considering the current coin)
               # 2. dp[x - coin] + 1 (minimum coins needed for the remaining amount (x - coin) plus the current coin)
               dp[x] = min(dp[x], dp[x - coin] + 1)
       
       # If dp[amount] is still max_value, it means the target amount cannot be made up by any combination of the coins
       # In that case, return -1 to indicate that it's not possible to make the change
       # Otherwise, return dp[amount], which represents the minimum number of coins needed
       return dp[amount] if dp[amount] != max_value else -1