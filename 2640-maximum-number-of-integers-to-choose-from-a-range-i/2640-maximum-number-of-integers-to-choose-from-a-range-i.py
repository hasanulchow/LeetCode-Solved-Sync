class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        """
        Determines the maximum number of integers from 1 to `n` that can be selected such that:
        - None of the selected integers are in the `banned` list.
        - The sum of the selected integers does not exceed `maxSum`.

        The strategy is to iterate through the integers from 1 to `n`, and for each integer,
        check if it is not banned and if adding it to the current sum would not exceed `maxSum`.
        We select as many integers as possible while keeping track of the sum.

        The function returns the maximum number of integers that can be selected under these conditions.
        """

        # Convert the `banned` list to a set for O(1) lookups.
        banned_set = set(banned)

        # Initialize `sum` (to keep track of the sum of selected integers) and `count` (to keep track of how many integers are selected).
        total_sum, count = 0, 0
        
        # Iterate through all integers from 1 to n.
        for i in range(1, n + 1):
            # If the integer `i` is not in the banned set and adding it to the sum doesn't exceed maxSum:
            if i not in banned_set and total_sum + i <= maxSum:
                count += 1  # Select the integer (increment the count).
                total_sum += i  # Add it to the sum.

        # Return the total count of selected integers.
        return count
