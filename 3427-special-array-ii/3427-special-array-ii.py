class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # Step 1: Initialize variables
        n = len(nums)  # Length of the nums array
        prev = nums[0] & 1  # Determine the parity (0 for even, 1 for odd) of the first element
        sameParity = [0] * n  # Array to store same-parity segment IDs
        j = 0  # Segment counter

        # Step 2: Identify contiguous segments of the same parity in nums
        for i in range(n):
            x = nums[i] & 1  # Determine the parity of the current number
            if x == prev:  # If parity is the same as the previous number
                j += 1  # Increment the segment counter
            sameParity[i] = j  # Assign the segment ID to the current index
            prev = x  # Update the previous parity

        # Step 3: Process the queries
        m = len(queries)  # Number of queries
        ans = [False] * m  # Initialize the result list with False

        for i, (s, t) in enumerate(queries):
            # Check if the indices s and t belong to the same parity segment
            ans[i] = (sameParity[s] == sameParity[t])

        # Step 4: Return the results
        return ans
