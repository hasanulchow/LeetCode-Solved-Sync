class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Count the number of zeroes in the input list
        x = nums.count(0)
        
        # If the number of zeroes is greater than k, sort the list
        # and remove the extra zeroes so that only k zeroes remain
        if x > k:
            nums.sort()
            while nums.count(0) != k:
                nums.pop(0)  # Remove the first zero to make the count equal to k

        ind = 0
        dp = {}  # Dictionary to store computed subproblems
        return self.splitArrayHelper(nums, ind, k, dp)

    def splitArrayHelper(self, nums, ind, k, dp):
        # Base case: If k == 1, return the sum of the remaining part of the array
        if k == 1:
            return sum(nums[ind:len(nums)])

        # Check if the subproblem has already been solved (memoization)
        if (ind, k) in dp:
            return dp[(ind, k)]

        ans = float('inf')  # Initialize the answer to a large value
        sumi = 0  # To store the sum of the current segment
        
        # Try splitting the array at every possible position
        for i in range(ind, len(nums)):
            sumi += nums[i]  # Add the current number to the sum of the segment
            # Recursively calculate the maximum sum of the subarray and update the answer
            ans = min(ans, max(sumi, self.splitArrayHelper(nums, i+1, k-1, dp)))
        
        # Memoize the result for the current subproblem
        dp[(ind, k)] = ans
        return ans
