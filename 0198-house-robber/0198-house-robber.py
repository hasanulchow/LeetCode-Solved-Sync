class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Determines the maximum amount of money that can be robbed without robbing two adjacent houses.

        Args:
        nums (List[int]): A list of integers where each integer represents the amount of money in a house.

        Returns:
        int: The maximum amount of money that can be robbed.
        """
        n = len(nums)
        
        # Edge case: If there's only one house, rob it.
        if n == 1:
            return nums[0]
        
        # Initialize a dynamic programming array to store the maximum amount of money robbed up to each house.
        dp = [0] * n
        dp[0] = nums[0]  # If there's only one house, rob it.
        dp[1] = max(dp[0], nums[1])  # For two houses, choose the one with the maximum money.
        
        # Iterate through the list, starting from the third house.
        for i in range(2, n):
            # For each house, decide whether to rob this house or skip it.
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        # The last element in dp represents the maximum amount that can be robbed up to the last house.
        return dp[n-1]
