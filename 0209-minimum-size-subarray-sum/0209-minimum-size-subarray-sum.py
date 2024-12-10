class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Finds the minimal length of a contiguous subarray of which the sum is greater than or equal to `target`.
        Returns 0 if no such subarray exists.

        Args:
        target (int): The target sum.
        nums (List[int]): The input array.

        Returns:
        int: The minimal length of a qualifying subarray, or 0 if none exists.
        """
        s, l, ans = 0, 0, float('inf')  # Use `float('inf')` for comparison

        for r, val in enumerate(nums):
            s += val  # Expand the window to the right
            while s >= target:  # Shrink the window from the left
                ans = min(ans, r - l + 1)
                s -= nums[l]
                l += 1

        return ans if ans != float('inf') else 0  # Return 0 if no valid subarray was found
