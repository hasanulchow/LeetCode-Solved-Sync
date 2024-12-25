from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0  # Left pointer starts at the beginning of the list
        right = len(nums) - 1  # Right pointer starts at the end of the list

        while left < right:  # Continue the search while left pointer is less than right pointer
            mid = (left + right) // 2  # Calculate the middle index

            if nums[mid] <= nums[right]:  # If the middle element is less than or equal to the rightmost element
                right = mid  # The minimum must be in the left half (including mid)
            else:  # If the middle element is greater than the rightmost element
                left = mid + 1  # The minimum must be in the right half (excluding mid)

        return nums[left]  # After the loop, left points to the smallest element
