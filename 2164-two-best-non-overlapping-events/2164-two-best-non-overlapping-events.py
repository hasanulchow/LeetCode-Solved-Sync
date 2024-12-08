from bisect import bisect_right
from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Step 1: Sort the events by their start times
        events.sort()

        # Step 2: Initialize a variable to store the maximum value
        maxValue = 0
        n = len(events)

        # Step 3: Create a list of start times for all events
        startTimes = [events[i][0] for i in range(n)]

        # Step 4: Initialize a list to store the maximum value of events after each event
        suffixValues = [0] * n

        # Step 5: Set the last event's value in the suffix array
        suffixValues[-1] = events[-1][2]

        # Step 6: Populate the suffixValues array with maximum values of future events
        for i in reversed(range(n-1)):
            suffixValues[i] = max(events[i][2], suffixValues[i+1])

        # Step 7: Iterate through each event and find the best value by checking non-overlapping events
        for i, start in enumerate(startTimes):
            # Step 7a: Use binary search to find the first event that starts after the current event ends
            best_idx = bisect_right(startTimes, events[i][1], lo=i+1)

            # Step 7b: Calculate the value for the current event
            val = events[i][2]

            # Step 7c: If there are any valid events after the current one, add their value
            if best_idx < n:
                val += suffixValues[best_idx]

            # Step 7d: Update the maximum value found
            maxValue = max(maxValue, val)

        # Step 8: Return the maximum value found
        return maxValue
