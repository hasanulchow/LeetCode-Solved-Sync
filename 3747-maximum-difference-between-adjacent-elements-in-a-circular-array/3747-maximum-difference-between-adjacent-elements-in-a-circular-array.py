from typing import List
from itertools import pairwise

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        # Compute the maximum absolute difference between:
        # 1. The first and last elements of the list (nums[0] - nums[-1])
        # 2. All adjacent pairs in the list (e.g., abs(nums[i] - nums[i+1]) for all valid i)

        # pairwise(nums) creates pairs like (nums[0], nums[1]), (nums[1], nums[2]), etc.
        # We calculate the absolute difference for each adjacent pair
        max_adjacent_diff = max(abs(x - y) for x, y in pairwise(nums))

        # Also compute the absolute difference between the first and last element
        edge_diff = abs(nums[0] - nums[-1])

        # Return the maximum of the two computed differences
        return max(edge_diff, max_adjacent_diff)
