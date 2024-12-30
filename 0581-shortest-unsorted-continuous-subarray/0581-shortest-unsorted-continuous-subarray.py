class Solution:
    def findUnsortedSubarray(self, nums):
        sorted_nums = sorted(nums)
        start = next( (i for i in range(len(nums)) if nums[i]!=sorted_nums[i]), None)
        end = next( (i for i in range(len(nums)-1,-1,-1) if nums[i]!=sorted_nums[i]), None)
        return end - start + 1 if start is not None else 0