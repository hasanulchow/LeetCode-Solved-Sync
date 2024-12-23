class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1  # Initialize the search range

        while start < end:  # Continue searching while start is less than end
            mid = (start + end) // 2  # Find the middle element

            if nums[mid] > nums[end]:  # If mid element is greater than the end element, the min is in the right half
                start = mid + 1
            elif nums[mid] < nums[start]:  # If mid element is less than the start element, the min is in the left half
                end = mid
            else:  # If mid element equals the start element, reduce the search range by moving end left
                end -= 1

        return nums[start]  # Return the element at the start index, which is the minimum
