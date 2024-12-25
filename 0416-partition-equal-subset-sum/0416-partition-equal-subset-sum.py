class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s&1:
            return False
        """
        The dp array stores the total obtained sums we have come across so far.
        Notice that dp[0] = True; if we never select any element, the total sum is 0.
        """
        dp = [True]+[False]*s
        # Now, loop through each element
        for num in nums:
            for curr in range(s, num-1, -1):  # avoid going out-of-bounds
                """
                Case 1: The current sum (curr) has been seen before.
                        Then, if we don't select the current element, the sum will not change.
						So, this total sum will still exist, and its dp value remains True.
				
				Case 2: The current sum (curr) has not been seen before,
				        but it can be obtained by selecting the current element.
						This means that dp[curr-num] = True, and thus dp[curr] now becomes True.
				
				Case 3: The current sum (curr) has not been seen before,
				        and it cannot be obtained by selecting the current element.
						So, this total sum will still not exist, and its dp value remains False.
                """
                dp[curr] = dp[curr] or dp[curr-num]
        # Finally, we want to obtain the target sum
        return dp[s//2]  # or dp[s>>1]