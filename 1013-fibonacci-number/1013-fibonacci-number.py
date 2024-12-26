class Solution:
    def fib(self, n: int) -> int:
        # Base case: if n is 0 or 1, return n directly
        if n <= 1:
            return n

        # Initialize the first two Fibonacci numbers
        a, b = 0, 1

        # Compute Fibonacci numbers iteratively from 2 to n
        for _ in range(2, n + 1):
            # Update `a` to the previous `b`, and `b` to the sum of `a` and `b`
            a, b = b, a + b

        # Return the nth Fibonacci number
        return b
