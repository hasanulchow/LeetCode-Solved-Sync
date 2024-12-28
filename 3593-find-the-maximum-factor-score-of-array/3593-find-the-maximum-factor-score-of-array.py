class Solution:
    def maxScore(self, nums: List[int]) -> int:
        ans=gcd(*nums)*lcm(*nums) #whole array
        for i in range(len(nums)):
            temp=(nums[:i]+nums[i+1:]) #skipping ith index
            g=gcd(*temp)
            l=lcm(*temp)
            ans=max(ans,l*g)
        return ans