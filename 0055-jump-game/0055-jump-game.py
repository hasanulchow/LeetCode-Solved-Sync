class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Determines if you can reach the last index of the `nums` list, starting from the first index.
        Each element in the list represents the maximum number of steps you can jump forward from that index.
        The goal is to check if there exists a way to jump from the start to the last index.

        The strategy is to maintain a variable `mx` (maximum reachable index), and at each step, update it 
        based on the current position and the jump length at that position. If at any point the maximum reachable
        index does not extend beyond the current position, it means we are stuck and cannot reach the end.
        """

        # `mx` keeps track of the farthest index we can reach so far.
        # Initialize `mx` to 0 because at the start, the farthest we can reach is the first index.
        # `n` is the length of the list `nums`.
        mx, n = 0, len(nums)
        
        # Loop through each index `i` in the list.
        for i in range(n):
            # If the current index `i` is beyond the maximum reachable index, we cannot proceed.
            # Hence, if `i > mx`, return False immediately.
            if i > mx:
                return False

            # Update `mx` to the maximum of its current value and the farthest we can reach from index `i`.
            mx = max(mx, nums[i] + i)

            # If we have reached or exceeded the last index, we can jump to the end, so return True.
            if mx >= n - 1:
                return True

        # If the loop finishes without returning True, it means we cannot reach the last index.
        return False
