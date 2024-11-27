import heapq
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # Two heaps (min-heaps) to store the costs from both ends of the array
        h1 = []  # Min-heap for the first `candidates` elements
        h2 = []  # Min-heap for the last `candidates` elements
        res = []  # List to store the k smallest costs we will select

        n = len(costs)
        i, j = 0, n - 1  # Two pointers, i at the beginning and j at the end

        while len(res) < k:  # We need to select `k` elements
            # Push elements from the start (left side) into h1 until we have `candidates` elements
            while len(h1) < candidates and i <= j:
                heapq.heappush(h1, (costs[i], i))  # Push the cost and the index
                i += 1  # Move the pointer i to the right

            # Push elements from the end (right side) into h2 until we have `candidates` elements
            while len(h2) < candidates and i <= j:
                heapq.heappush(h2, (costs[j], j))  # Push the cost and the index
                j -= 1  # Move the pointer j to the left

            # Now, choose the smaller cost from either heap h1 or h2
            if h1 and h2:
                if h1[0][0] <= h2[0][0]:
                    val = heapq.heappop(h1)  # Pop the smallest from h1
                else:
                    val = heapq.heappop(h2)  # Pop the smallest from h2
            elif h1:  # If only h1 has elements left
                val = heapq.heappop(h1)
            elif h2:  # If only h2 has elements left
                val = heapq.heappop(h2)

            res.append(val[0])  # Append the cost value to the result

        # Return the sum of the k selected costs
        return sum(res)
