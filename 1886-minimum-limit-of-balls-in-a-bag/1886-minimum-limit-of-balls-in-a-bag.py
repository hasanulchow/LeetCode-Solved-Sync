class Solution:
    # Function to determine the minimum size of the largest box after making at most maxOperations splits
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        # Helper function to check if it's possible to achieve a given penalty size with maxOperations splits
        def canAchievePenalty(penalty):
            operations = 0  # Variable to keep track of the number of splits needed
            for balls in nums:  # Loop over each box in nums
                if balls > penalty:  # If a box has more balls than the allowed penalty size
                    # Calculate how many splits we need for this box to make the size <= penalty
                    operations += (balls - 1) // penalty  # (balls - 1) // penalty gives the number of splits required
            # Return True if total operations <= maxOperations, otherwise False
            return operations <= maxOperations

        # Binary search initialization:
        left, right = 1, max(nums)  # Search for penalty size in the range [1, max(nums)]
        
        # Binary search loop to narrow down the minimum penalty size
        while left < right:  # Continue as long as left < right (we haven't narrowed down the answer)
            mid = (left + right) // 2  # Find the middle of the current search range
            # Check if it's possible to achieve the penalty size 'mid' with maxOperations
            if canAchievePenalty(mid):
                right = mid  # If possible, try for a smaller penalty (narrow the search range to [left, mid])
            else:
                left = mid + 1  # If not possible, we need a larger penalty (narrow the search range to [mid + 1, right])

        # After the binary search loop ends, 'left' will be the smallest penalty size that works
        return left
