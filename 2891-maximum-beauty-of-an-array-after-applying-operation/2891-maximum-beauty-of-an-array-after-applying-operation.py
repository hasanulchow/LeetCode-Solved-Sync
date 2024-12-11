class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # Sort the array to make it easier to find valid ranges
        nums.sort()

        # Get the length of the nums array
        n = len(nums)

        # Initialize the left pointer of the window
        left = 0

        # Initialize the variable to track the maximum "beauty"
        ans = 0

        # Iterate through the array using the index and value
        for i, num in enumerate(nums):
            # Adjust the left pointer to maintain the condition that the difference
            # between nums[i] and nums[left] is at most 2 * k
            while left < n and nums[left] < num - 2 * k:
                left += 1

            # Update the maximum beauty value (length of the valid range)
            ans = max(ans, i - left + 1)

        # Return the maximum beauty
        return ans
