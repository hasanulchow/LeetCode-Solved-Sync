class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit that can be achieved by buying and selling
        a stock at most once. The function assumes you can only make one buy and one sell
        and the buy must happen before the sell.

        The strategy is to track the minimum price encountered so far, and at each step, 
        compute the potential profit if the stock were sold at the current price.
        """
        
        # Initialize `max_profit` to 0 because no profit can be made initially.
        max_profit = 0
        
        # Set the initial minimum price as the first price in the list.
        min_price = prices[0]

        # Loop through the list of prices starting from the second price.
        for price in prices[1:]:
            # Calculate the potential profit if we sell at the current `price`.
            potential_profit = price - min_price

            # Update `max_profit` if the current potential profit is greater than the previous `max_profit`.
            max_profit = max(max_profit, potential_profit)

            # Update `min_price` if the current `price` is lower than the previous `min_price`.
            min_price = min(min_price, price)

        # Return the maximum profit found.
        return max_profit
