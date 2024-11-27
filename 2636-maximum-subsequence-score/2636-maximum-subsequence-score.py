from typing import List
from heapq import heappop, heappush
from operator import itemgetter

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res, prefixSum, minHeap = 0, 0, []
        
        # Zip nums1 and nums2 together and sort by the second array (nums2) in descending order
        for a, b in sorted(zip(nums1, nums2), key=itemgetter(1), reverse=True):
            # Add the current element from nums1 to the prefix sum
            prefixSum += a
            # Add the element to the min-heap to maintain the top k elements
            heappush(minHeap, a)
            
            # If we have more than k elements in the heap, remove the smallest
            if len(minHeap) > k:
                prefixSum -= heappop(minHeap)
            
            # If we have exactly k elements in the heap, calculate the score and update result
            if len(minHeap) == k:
                res = max(res, prefixSum * b)
        
        return res

        