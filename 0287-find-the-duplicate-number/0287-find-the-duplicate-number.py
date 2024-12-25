class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            ind = abs(nums[i])
            if nums[ind] < 0:
                return ind
            nums[ind] = -nums[ind]
        return -1