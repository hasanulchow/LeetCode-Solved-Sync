class Solution:
    def maxArea(self, height):
        max_area = 0  # Initialize the variable to store the maximum area
        left = 0  # Left pointer, starting at the beginning of the list
        right = len(height) - 1  # Right pointer, starting at the end of the list

        # Use a two-pointer approach
        while left < right:
            # Calculate the area formed by the lines at the left and right pointers
            current_area = min(height[left], height[right]) * (right - left)
            
            # Update the max_area if the current_area is larger
            max_area = max(max_area, current_area)
            
            # Move the pointer with the smaller height inward to try to find a larger area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area  # Return the maximum area found
