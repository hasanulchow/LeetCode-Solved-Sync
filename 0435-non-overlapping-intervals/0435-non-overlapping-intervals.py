class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Initialize the counter 'rs' to keep track of the number of intervals to remove
        rs = 0
        
        # Sort intervals based on the end time of each interval (x[1])
        # This helps in selecting the interval that finishes the earliest, which can 
        # leave room for the maximum number of non-overlapping intervals.
        intervals.sort(key=lambda x: x[1])
        
        # Set the 'end' to a very small value initially, which will track the end time 
        # of the last selected interval.
        end = float('-inf')
        
        # Loop through each interval in the sorted list
        for interval in intervals:
            # If the start of the current interval is less than the 'end', it means 
            # this interval overlaps with the previous one, so we need to remove it.
            if interval[0] < end:
                # Increment the counter 'rs' since we are "removing" this overlapping interval
                rs += 1
            else:
                # If there's no overlap, we update 'end' to the end of the current interval
                end = interval[1]

        # Return the number of intervals we need to remove to make the rest non-overlapping
        return rs

        