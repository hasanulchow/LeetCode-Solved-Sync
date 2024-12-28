class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums)
        
        @cache
        def fn(i, op1, op2): 
            """Return """
            if i == n: return 0 
            ans = nums[i] + fn(i+1, op1, op2)
            if op1: ans = min(ans, (nums[i]+1)//2 + fn(i+1, op1-1, op2))
            if op2 and nums[i] >= k: ans = min(ans, nums[i]-k + fn(i+1, op1, op2-1))
            if op1 and op2 and (nums[i]+1)//2 >= k: ans = min(ans, (nums[i]+1)//2-k + fn(i+1, op1-1, op2-1))
            if op1 and op2 and nums[i] >= k: ans = min(ans, (nums[i]-k+1)//2 + fn(i+1, op1-1, op2-1))
            return ans 
        
        return fn(0, op1, op2)