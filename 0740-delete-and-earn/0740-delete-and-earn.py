class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # Handle edge case: if the input list is empty, return 0
        if not nums:
            return 0

        # Create a frequency array where each index represents the number,
        # and its value is the sum of all occurrences of that number in the input.
        freq = [0] * (max(nums) + 1)
        for n in nums:
            freq[n] += n

        # Initialize the dynamic programming array `dp`.
        # dp[i] represents the maximum points obtainable up to the number `i`.
        dp = [0] * len(freq)

        # Base cases:
        dp[1] = freq[1]  # The maximum points obtainable using only the number `1`.

        # Fill the `dp` array using the recurrence relation:
        # dp[i] = max(freq[i] + dp[i-2], dp[i-1])
        # This accounts for whether we "take" the current number or "skip" it.
        for i in range(2, len(freq)):
            dp[i] = max(freq[i] + dp[i - 2], dp[i - 1])

        # The last element in `dp` contains the maximum points we can earn.
        return dp[len(freq) - 1]
