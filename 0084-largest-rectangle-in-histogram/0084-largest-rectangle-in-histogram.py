class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Goal: Find the largest rectangle area in a histogram represented by the list `heights`.

        Approach: 
        - Use a stack to efficiently track the heights of the histogram bars and their indices.
        - We process each height from left to right, maintaining the stack to store indices of bars in increasing order of height.
        - When we encounter a bar that is shorter than the bar represented by the index at the top of the stack, we calculate the potential rectangle area using the bar at the top of the stack as the shortest bar.
        - The width of the rectangle is determined by the difference between the current index and the index of the bar just below the top of the stack.
        - After processing all bars, we may still have indices in the stack that need to be processed.

        Steps:
        1) Initialize a stack with -1 to handle edge cases and to simplify calculation of width.
        2) Traverse through each bar's height in `heights`:
            - While the current height is smaller than or equal to the height of the bar at the top of the stack, pop from the stack and calculate the rectangle area formed with the popped height as the shortest bar.
            - Push the current index onto the stack.
        3) After processing all bars, empty the stack by calculating the area for any remaining bars.

        Time Complexity: O(n) where n is the number of bars in `heights` (due to each index being pushed and popped from the stack at most once).
        Space Complexity: O(n) for the stack used to store the indices.

        Example:
        Input: heights = [2, 1, 5, 6, 2, 3]
        Output: 10 (the largest rectangle has area 10, formed by heights[2] and heights[3], width = 2)
        """
        
        stack = [-1]  # Stack to store indices, initialized with -1 to simplify width calculation
        max_area = 0  # Variable to keep track of the maximum area

        # Traverse through each height in the histogram
        for i in range(len(heights)):
            # While the current bar is shorter than the bar at the top of the stack
            while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                # Pop the stack and calculate area with the popped height as the shortest
                height = heights[stack.pop()]
                width = i - stack[-1] - 1  # Width is the difference between current index and the last index in the stack
                max_area = max(max_area, height * width)  # Update max_area if the new area is larger
            # Push the current index onto the stack
            stack.append(i)
        
        # After processing all bars, empty the stack
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1  # Width is from the current index to the end of the histogram
            max_area = max(max_area, height * width)  # Update max_area
        
        return max_area  # Return the maximum area found
