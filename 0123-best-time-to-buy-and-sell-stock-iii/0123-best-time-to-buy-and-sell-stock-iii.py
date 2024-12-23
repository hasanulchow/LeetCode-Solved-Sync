class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        This function calculates the maximum profit you can achieve by buying and selling stock at most twice.

        Approach:
        1. We use dynamic programming with four variables to track the state:
           - `first_buy`: The maximum profit we can achieve after the first buy.
           - `first_sell`: The maximum profit we can achieve after the first sell.
           - `second_buy`: The maximum profit we can achieve after the second buy.
           - `second_sell`: The maximum profit we can achieve after the second sell.
        
        2. We iterate through the list of stock prices:
           - For `first_buy`, we track the maximum value of `first_buy` as the negative price, as we're buying.
           - For `first_sell`, we track the maximum value of `first_sell` as the difference between the current price and the first buy.
           - For `second_buy`, we track the maximum value of `second_buy` as the difference between the first sell and the current price.
           - For `second_sell`, we track the maximum value of `second_sell` as the difference between the current price and the second buy.

        3. Finally, `second_sell` holds the maximum profit we can make by performing at most two transactions.

        Time Complexity: O(n), where `n` is the length of the prices list. We iterate over the list once.
        Space Complexity: O(1) as we are using a constant amount of space for tracking the states.
        """
        
        # If no prices are given, no transactions can be made
        if not prices:
            return 0
        
        # Initialize variables to track the profit at each stage
        first_buy = float('-inf')  # Maximum profit after the first buy (initially negative infinity)
        first_sell = 0             # Maximum profit after the first sell (initially 0)
        second_buy = float('-inf') # Maximum profit after the second buy (initially negative infinity)
        second_sell = 0            # Maximum profit after the second sell (initially 0)
        
        # Iterate through all the prices to calculate the maximum profit
        for price in prices:
            # Max profit after the first buy: either no buy or buying at the current price
            first_buy = max(first_buy, -price)
            
            # Max profit after the first sell: either no sell or selling at the current price
            first_sell = max(first_sell, first_buy + price)
            
            # Max profit after the second buy: either no second buy or buying after the first sell
            second_buy = max(second_buy, first_sell - price)
            
            # Max profit after the second sell: either no second sell or selling at the current price
            second_sell = max(second_sell, second_buy + price)
        
        # The result is the maximum profit after the second sell, i.e., after two transactions
        return second_sell

# Test the function with sample inputs
solution = Solution()
print(solution.maxProfit([3,3,5,0,0,3,1,4]))  # Example where the maximum profit is 6
print(solution.maxProfit([1,2,3,4,5]))         # Example where the maximum profit is 4
print(solution.maxProfit([7,6,4,3,1]))         # Example where no profit can be made
