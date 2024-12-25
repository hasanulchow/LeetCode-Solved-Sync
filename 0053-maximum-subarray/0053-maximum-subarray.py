class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Finds the maximum sum of a contiguous subarray in the given array.

        Args:
        nums (List[int]): List of integers.

        Returns:
        int: The maximum sum of a contiguous subarray.
        """
        # Initialize result with the first element of nums
        res = nums[0]
        
        # Initialize the current running total to 0
        total = 0

        # Iterate through each number in the array
        for n in nums:
            # If the running total is negative, reset it to 0
            # This means we start a new subarray from the current number
            if total < 0:
                total = 0

            # Add the current number to the running total
            total += n

            # Update the result with the maximum of the current result and running total
            res = max(res, total)
        
        # Return the maximum subarray sum
        return res
