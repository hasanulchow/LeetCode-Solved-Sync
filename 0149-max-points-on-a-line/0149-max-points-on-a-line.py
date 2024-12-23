from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        points.sort()  # Sort the points to ensure consistency (helps avoid floating point issues with slope calculation)
        
        slope, M = defaultdict(int), 0  # 'slope' stores the count of each unique slope, 'M' tracks the max number of points on a line
        
        for i, (x1, y1) in enumerate(points):  # Iterate through each point
            slope.clear()  # Clear the slope dictionary for each new base point
            
            for x2, y2 in points[i + 1:]:  # Compare the current point (x1, y1) with all points that come after it
                dx, dy = x2 - x1, y2 - y1  # Calculate the differences in x and y coordinates
                
                # Get the greatest common divisor to normalize the slope
                G = gcd(dx, dy)
                m = (dx // G, dy // G)  # Normalize the slope (dx, dy) by dividing by their GCD
                
                slope[m] += 1  # Increment the count of the normalized slope
                if slope[m] > M:  # Update the maximum number of points on the same line if needed
                    M = slope[m]
        
        return M + 1  # Return the maximum count of points on the same line, adding 1 to include the base point itself
