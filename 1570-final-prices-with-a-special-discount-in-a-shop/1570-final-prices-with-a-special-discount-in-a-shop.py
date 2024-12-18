class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        Adjusts each item's price in the 'prices' list by subtracting the price of the 
        next item of equal or lesser value (if such an item exists). 
        
        :param prices: List[int] - A list of integers representing the prices of items.
        :return: List[int] - A list where each price is adjusted according to the discount.
        """
        
        # Iterate through each item in the prices list
        for i in range(len(prices)):
            # Check subsequent items to find the first one that is less than or equal to the current item's price
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    # Apply the discount and break the loop once the first valid discount is found
                    prices[i] -= prices[j]
                    break
        
        # Return the updated list with discounted prices
        return prices
