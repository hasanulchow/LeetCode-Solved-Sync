'''
- formula for finding area when points are given
    1/2 * ( ∣x1×(y2−y3)+x2×(y3−y1)+x3×(y1−y2)∣ )
- okay let's try for all combinations of three points
- for three points we need three pointers so three for loops
'''
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # Initialize the variable to store the maximum area found
        max_area = 0
        
        # Get the number of points
        n = len(points)
        
        # Iterate over all combinations of three different points
        for p1 in range(n-2):  # First point (start from 0 up to n-3)
            for p2 in range(p1+1, n-1):  # Second point (start from p1+1 to n-2)
                for p3 in range(p2+1, n):  # Third point (start from p2+1 to n-1)
                    # Extract coordinates of the three points
                    x1, y1 = points[p1]
                    x2, y2 = points[p2]
                    x3, y3 = points[p3]
                    
                    # Calculate the area of the triangle using the determinant formula
                    area = 1/2 * abs(
                        x1 * (y2 - y3) + 
                        x2 * (y3 - y1) + 
                        x3 * (y1 - y2)
                    )
                    
                    # Update max_area if the calculated area is larger
                    max_area = max(max_area, area)
        
        # Return the largest area found (float value)
        return max_area