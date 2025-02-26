class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr, max_val = 0, float('-inf')
        n = len(nums)

        for i in range(n):
            curr = max(0, curr + nums[i])
            max_val = max(max_val, curr)

        curr, min_val = 0, float('inf')
        
        for i in range(n - 1, -1, -1):
            curr = min(0, curr + nums[i])
            min_val = min(min_val, curr)
        
        return max(max_val, abs(min_val))