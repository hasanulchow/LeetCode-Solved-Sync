class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # Initialize variables:
        # cnt to count the number of chunks,
        # diff to track the cumulative difference between values and indices
        cnt = 0
        diff = 0

        # Iterate through the array with both index and value
        for i, x in enumerate(arr):
            # Update the cumulative difference
            diff += x - i

            # If the cumulative difference is 0, it means we can split here
            cnt += (diff == 0)

        # Return the total number of chunks
        return cnt
