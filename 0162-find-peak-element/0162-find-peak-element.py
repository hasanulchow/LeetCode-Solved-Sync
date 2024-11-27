from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Initialize two pointers, left and right, to the start and end of the list, respectively
        left = 0
        right = len(nums) - 1
        
        # Perform binary search to find the peak element
        while left < right:
            # Calculate the midpoint of the current search range
            mid = (left + right) // 2
            
            # Check if the middle element is greater than the next element
            if nums[mid] > nums[mid + 1]:
                # If nums[mid] > nums[mid+1], it means the peak element is in the left half,
                # so move the right pointer to mid
                right = mid
            else:
                # If nums[mid] <= nums[mid+1], it means the peak element is in the right half,
                # so move the left pointer to mid + 1
                left = mid + 1
        
        # At the end of the loop, left will point to the peak element
        return left
