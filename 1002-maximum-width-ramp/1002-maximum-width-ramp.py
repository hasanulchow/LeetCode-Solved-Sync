class Solution:
    def maxWidthRamp(self, nums):
        ans = 0
        n = len(nums)

        # Create a list of tuples (element, index)
        vp = [(nums[i], i) for i in range(n)]

        # Sort the list based on the element values
        vp.sort()

        # Keep track of the minimum index seen so far
        min_index = vp[0][1]

        # Traverse the sorted list to calculate the maximum width ramp
        for i in range(1, n):
            current_index = vp[i][1]
            ans = max(ans, current_index - min_index)
            min_index = min(min_index, current_index)

        return ans