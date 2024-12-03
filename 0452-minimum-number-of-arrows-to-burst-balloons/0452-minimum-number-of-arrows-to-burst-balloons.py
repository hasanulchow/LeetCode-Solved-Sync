class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort the intervals by their end position (second value of each point)
        # Sorting by the end time ensures that we can shoot the arrow as late as possible,
        # maximizing the chance of hitting multiple intervals with one arrow.
        points = sorted(points, key = lambda x: x[1])
        
        # Initialize 'end' as None to signify that no arrow has been shot yet
        # 'count' keeps track of the number of arrows needed.
        end = None
        count = 0
        
        # Iterate through the sorted intervals
        for p in points:
            # If the current interval's start position is after the last arrow's end position,
            # it means the current interval does not overlap with the previous ones.
            # We need a new arrow to burst this balloon, so we update 'end' to the current interval's end
            # and increment the arrow count.
            if end is None or end < p[0]:
                end = p[1]  # Shoot a new arrow to cover this interval
                count += 1   # Increment the number of arrows used
        
        # Return the total number of arrows needed
        return count

        