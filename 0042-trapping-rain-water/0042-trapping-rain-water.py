class Solution:
    # Function to calculate the amount of rainwater trapped between bars
    def trap(self, height: List[int]) -> int:
        # Initialize the left wall and right wall (used for calculating max heights)
        l_wall = r_wall = 0
        # Get the length of the height list
        n = len(height)
        
        # Arrays to store the maximum height encountered from left to right (max_left)
        # and from right to left (max_right) for each index.
        max_left = [0] * n
        max_right = [0] * n
        
        # Traverse the height list from left to right and fill max_left and max_right arrays
        for i in range(n):
            # Calculate the index from the right side (reverse index)
            j = -i - 1  # This calculates the corresponding index from the right
            
            # Update max_left for the current index (i) with the max left wall encountered so far
            max_left[i] = l_wall
            # Update max_right for the current reverse index (j) with the max right wall encountered so far
            max_right[j] = r_wall
            
            # Update the left wall with the max height encountered up to this point
            l_wall = max(l_wall, height[i])
            # Update the right wall with the max height encountered up to this point from the right
            r_wall = max(r_wall, height[j])
        
        # Variable to accumulate the total trapped water
        summ = 0
        
        # Traverse the height list again to calculate the trapped water at each index
        for i in range(n):
            # The amount of water that can be trapped at index 'i' is determined by the shorter of 
            # the maximum walls from the left and right minus the height of the current bar.
            pot = min(max_left[i], max_right[i])
            # Add the trapped water at the current position (if any, i.e., if height[i] < pot)
            summ += max(0, pot - height[i])
        
        # Return the total trapped water
        return summ
