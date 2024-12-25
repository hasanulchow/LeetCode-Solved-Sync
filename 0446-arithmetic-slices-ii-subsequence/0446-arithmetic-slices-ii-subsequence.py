from collections import defaultdict
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        Counts the number of arithmetic subsequences in the array.
        
        Args:
        nums (List[int]): List of integers representing the input array.
        
        Returns:
        int: The total count of arithmetic subsequences.
        """
        n = len(nums)  # Get the length of the input array.
        total_count = 0  # Initialize the total count of arithmetic subsequences.
        dp = [defaultdict(int) for _ in range(n)]  # Array of dictionaries to store counts of subsequences for each index.

        for i in range(1, n):
            for j in range(i):
                # Calculate the difference between nums[i] and nums[j].
                diff = nums[i] - nums[j]

                # Update the count of subsequences ending at index `i` with difference `diff`.
                dp[i][diff] += 1

                # If there are existing subsequences with the same difference ending at `j`,
                # extend those subsequences to include `nums[i]`.
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    # Add the count of subsequences extended from `j` to the total count.
                    total_count += dp[j][diff]

        return total_count
