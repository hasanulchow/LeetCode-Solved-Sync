class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        Calculates the number of trailing zeroes in the factorial of a given number.

        Args:
        n (int): The input number whose factorial's trailing zeroes are to be counted.

        Returns:
        int: The count of trailing zeroes in n!.
        """
        fives = 0  # Initialize a counter for multiples of 5
        i = 5      # Start with the smallest multiple of 5
        
        # Count the number of factors of 5 in the numbers from 1 to n
        while i <= n:
            fives += n // i  # Add the count of multiples of the current power of 5
            i *= 5          # Move to the next power of 5
        
        return fives
