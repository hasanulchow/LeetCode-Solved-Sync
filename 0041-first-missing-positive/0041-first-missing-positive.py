class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Place each number in its correct position if possible
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Step 2: Find the first index where the number is not in the correct position
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # Step 3: If all positions are correct, return n + 1
        return n + 1
