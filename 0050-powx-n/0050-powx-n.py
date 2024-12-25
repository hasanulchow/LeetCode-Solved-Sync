class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Calculates x raised to the power n (x^n) using recursion and divide-and-conquer.

        Args:
        x (float): The base number.
        n (int): The exponent.

        Returns:
        float: The result of x raised to the power n.
        """

        def calc_power(x, n):
            """
            Helper function to recursively calculate the power of x^n.
            """
            # Base cases
            if x == 0:  # If the base is 0, the result is 0 (0^n = 0 for n > 0)
                return 0
            if n == 0:  # Any number raised to the power 0 is 1
                return 1
            
            # Recursive step: calculate power for half the exponent
            res = calc_power(x, n // 2)
            res = res * res  # Square the result to handle half the power
            
            # If n is odd, multiply by x one more time
            if n % 2 == 1:
                return res * x
            
            return res

        # Calculate the absolute value of the exponent
        ans = calc_power(x, abs(n))

        # If n is negative, return the reciprocal; otherwise, return the result
        if n >= 0:
            return ans
        return 1 / ans
