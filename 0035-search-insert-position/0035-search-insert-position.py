from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0  # Left pointer to the start of the list
        right = len(nums) - 1  # Right pointer to the end of the list

        while left <= right:  # Continue the search while the left pointer is less than or equal to the right pointer
            mid = (left + right) // 2  # Calculate the middle index

            if nums[mid] == target:  # If the target is found at mid, return its index
                return mid
            elif nums[mid] > target:  # If the target is smaller than nums[mid], narrow the search to the left half
                right = mid - 1
            else:  # If the target is larger than nums[mid], narrow the search to the right half
                left = mid + 1

        return left  # If the target is not found, return the left pointer, which indicates the insert position
