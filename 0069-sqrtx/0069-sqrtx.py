class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Computes the integer square root of a given non-negative integer x.

        Args:
        x (int): The input number for which the square root is to be computed.

        Returns:
        int: The integer part of the square root of x.
        """
        # Special case: the square root of 0 is 0
        if x == 0:
            return 0
        
        # Initialize binary search boundaries
        left, right = 1, x
        
        # Perform binary search to find the integer square root
        while left <= right:
            mid = (left + right) // 2  # Calculate the middle value
            
            # Check if mid is the exact square root
            if mid * mid == x:
                return mid
            # If mid squared is less than x, search the right half
            elif mid * mid < x:
                left = mid + 1
            # If mid squared is greater than x, search the left half
            else:
                right = mid - 1
        
        # Return the largest integer whose square is less than or equal to x
        return right
