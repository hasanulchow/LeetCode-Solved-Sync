class StockSpanner:

    def __init__(self):
        # Initialize an empty stack to keep track of stock prices and their spans.
        self.stack = []
        

    def next(self, price: int) -> int:
        # Initialize the span to 1 because the minimum span for any stock is 1 (the stock itself).
        span = 1
        # This variable will store the span from the previous stack elements if they are smaller than the current price.
        last_span = 0
        
        # Pop elements from the stack while the stack is not empty and the current price is greater than or equal to the price in the stack.
        while self.stack and price >= self.stack[-1][0]:
            # Get the previous price and its span.
            value, last_span = self.stack.pop()
            # Add the span of the previous element to the current span.
            span += last_span
        
        # Push the current price and its span onto the stack.
        self.stack.append((price, span))
        
        # Return the span for the current price.
        return span
        

# Usage example:
# obj = StockSpanner()  # Instantiate the object
# param_1 = obj.next(price)  # Call the next() method to get the span of the given price.
