from collections import deque
from bisect import bisect_right
from operator import itemgetter
from typing import List

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # Initialize the result list with zeros and an empty list to store (a, b, i) tuples for future processing
        res, idx = [0] * len(queries), []

        # Process each query
        for i, q in enumerate(queries):
            a, b = sorted(q)  # Sort the two values in each query to ensure a < b
            if a == b or heights[a] < heights[b]:  # If the buildings are the same or height[a] < height[b]
                res[i] = b  # The answer for this query is b (the second building in sorted order)
            else:
                idx.append((a, b, i))  # Otherwise, store the query for future processing

        # Start processing the stored queries (a, b, i) in reverse order of b
        j, mono = len(heights) - 1, deque()  # j starts from the last building, mono is a deque to store indices
        for a, b, i in sorted(idx, key=itemgetter(1), reverse=True):  # Sort by b in descending order
            while j > b:
                # Process buildings in reverse order, adding buildings to mono if their height is greater than the current height
                while mono and heights[mono[0]] < heights[j]:
                    mono.popleft()  # Remove buildings from the front of deque if their height is smaller than the current building
                mono.appendleft(j)  # Add the current building to the deque
                j -= 1  # Move to the next building to the left
            
            # Perform binary search to find the leftmost building that is taller than building at position a
            k = bisect_right(mono, heights[a], key=lambda x: heights[x])
            res[i] = -1 if k == len(mono) else mono[k]  # If no such building is found, return -1, else return the index of the building
        
        # Return the list of results for all queries
        return res
