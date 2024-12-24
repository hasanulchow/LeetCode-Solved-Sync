class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize pointers for binary search
        left = 0
        right = len(nums) - 1

        # Perform binary search
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2

            # Check if the middle element is the target
            if nums[mid] == target:
                return mid
            
            # Determine if the left half is sorted
            if nums[mid] >= nums[left]:
                # Check if the target lies within the sorted left half
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1  # Search in the left half
                else:
                    left = mid + 1  # Search in the right half
            else:
                # Right half must be sorted
                # Check if the target lies within the sorted right half
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1  # Search in the right half
                else:
                    right = mid - 1  # Search in the left half
        
        # Target not found
        return -1
