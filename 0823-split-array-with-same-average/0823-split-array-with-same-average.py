class Solution:
    def splitArraySameAverage(self, nums):
        n, total = len(nums), sum(nums)

        @lru_cache(None)
        def function(i,target,k):
            if k == 0:
                return target == 0

            if k+i > n:
                return False 

            return function(i+1,target-nums[i],k-1) or function(i+1,target,k)

        for j in range(1,n//2+1):
            if function(0,total*j//n,j) and total*j%n == 0:
                return True 

        return False 