from heapq import *

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Negate all elements to simulate a max-heap (Python's heapq is a min-heap by default).
        gifts = [-i for i in gifts]
        heapify(gifts)  # Convert the list into a heap.
        
        # Perform the operation 'k' times.
        for i in range(k):
            current = heappop(gifts)  # Extract the largest element (negated value).
            # Calculate the square root of the absolute value of the current gift.
            current = int(abs(current) ** (1/2))
            # Push the new value (negated) back into the heap.
            heappush(gifts, -current)

        # Return the sum of the modified gifts (negating to restore original values).
        return -1 * sum(gifts)
