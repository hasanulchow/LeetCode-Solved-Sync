from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 2):  # Loop through possible subarray starts
            if nums[i] + nums[i + 2] == nums[i + 1] / 2:
                count += 1
        return count

# Example usage:
solution = Solution()
nums1 = [1, 2, 1, 4, 1]
nums2 = [1, 1, 1]
print(solution.countSubarrays(nums1))  # Output: 1
print(solution.countSubarrays(nums2))  # Output: 0
