from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []  # Result list to store all subsets
        subset = []  # Temporary list to store the current subset

        def create_subset(i):
            if i == len(nums):
                res.append(subset[:])  # Append a copy of the current subset to the result
                return
            
            # Include the current number (nums[i]) in the subset
            subset.append(nums[i])
            create_subset(i+1)  # Move to the next index with the current number included

            # Exclude the current number (backtrack) and try without it
            subset.pop()
            create_subset(i+1)  # Move to the next index without including the current number

        create_subset(0)  # Start creating subsets from index 0
        return res  # Return all the generated subsets
