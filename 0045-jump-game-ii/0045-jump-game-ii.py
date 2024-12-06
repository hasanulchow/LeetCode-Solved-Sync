class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Determines the minimum number of jumps required to reach the last index in the list `nums`.
        Each element in the list represents the maximum number of steps you can jump forward from that index.
        
        The strategy is to keep track of the farthest index we can reach within the current jump range.
        When we reach the end of the current jump range (`current_end`), we increase the jump count and extend the jump range 
        to the farthest index we can reach (`farthest`). This process continues until we reach or exceed the last index.

        The goal is to minimize the number of jumps required.
        """

        n = len(nums)
        jumps = 0  # To keep track of the number of jumps made.
        current_end = 0  # The farthest index we can reach with the current number of jumps.
        farthest = 0  # The farthest index we can reach by the end of the current jump.

        # Loop through each index in the list except the last one.
        for i in range(n - 1):  # We stop at `n-1` because we don't need to jump from the last index.
            # Update the farthest index we can reach from the current index.
            farthest = max(farthest, i + nums[i])

            # If we have reached the end of the current jump range, it's time to make a jump.
            if i == current_end:
                jumps += 1  # We make a jump.
                current_end = farthest  # Update the end of the current jump range.

                # If the current jump range reaches or exceeds the last index, we can stop here.
                if current_end >= n - 1:
                    break

        return jumps
