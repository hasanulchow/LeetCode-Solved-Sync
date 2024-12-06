class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit that can be achieved by buying and selling
        multiple times. The strategy is to capture all upward price movements and 
        treat them as separate buy/sell transactions. This way, you can maximize 
        profit by always "buying" at a lower price and "selling" at a higher price whenever possible.

        The idea is to simply accumulate the profit whenever there is an increase in price 
        from one day to the next, simulating multiple transactions.
        """
        
        # Initialize `profit` to 0, as no transactions have been made yet.
        profit = 0
        
        # Loop through the prices starting from the second price (index 1).
        for i in range(1, len(prices)):
            # If the current price is greater than the previous day's price,
            # we have a potential profit (buy on the previous day, sell on the current day).
            if prices[i] > prices[i-1]:
                # Accumulate the profit from this "buy-sell" transaction.
                profit += prices[i] - prices[i-1]

        # Return the total accumulated profit.
        return profit
