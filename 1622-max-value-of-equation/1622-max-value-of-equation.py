from heapq import heappush, heappop
from math import inf

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # Initialize the answer as negative infinity (since we're looking for a max)
        ans = -inf
        
        # Create a min-heap (priority queue)
        hp = [] 
        
        # Iterate through each point in the points list
        for xj, yj in points:
            # Remove points from the heap that are too far from the current point (xj - x' > k)
            while hp and xj - hp[0][1] > k:
                heappop(hp)
            
            # If the heap is not empty, calculate the maximum equation value
            if hp: 
                ans = max(ans, xj + yj - hp[0][0])
            
            # Push the current point (xj - yj, xj) into the heap
            heappush(hp, (xj - yj, xj))
        
        # Return the maximum value of the equation found
        return ans
