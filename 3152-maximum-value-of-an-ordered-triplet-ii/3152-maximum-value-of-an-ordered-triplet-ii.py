class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxNum = maxAns = maxDiff = 0
        for i in range(0, len(nums)):
            maxAns = max(maxAns, maxDiff * nums[i])
            maxDiff = max(maxDiff, maxNum - nums[i])
            maxNum = max(maxNum, nums[i])
        return maxAns