class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        # we can partition the array into two subsets with equal sum
        # only when the sum is even
        if s % 2: return False
        # k is our target sum
        k = s // 2
        # subset sum problem -> solve it with DP
        dp = [True] + [False] * k
        # for each number
        for x in nums:
            # check all number from k to x
            # to check if adding x can achieve i
            for i in range(k, x - 1, -1): dp[i] |= dp[i - x]
            # if dp[k] is achievable at a point, 
            # then we can return True
            if dp[k]: return True
        return dp[k]