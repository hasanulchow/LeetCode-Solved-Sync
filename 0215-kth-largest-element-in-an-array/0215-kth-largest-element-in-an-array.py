from heapq import heappush, heappop
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create an empty heap (min-heap by default in Python)
        heap = []

        # Iterate through each number in the input list 'nums'
        for i in nums:
            # Push the current number into the heap
            heappush(heap, i)

            # If the heap exceeds size 'k', remove the smallest element
            # This keeps the heap size constant at 'k'
            if len(heap) > k:
                heappop(heap)

        # The root of the heap will be the kth largest element after processing all numbers
        # Since it's a min-heap, the root holds the smallest element among the largest 'k' numbers
        return heappop(heap)

        