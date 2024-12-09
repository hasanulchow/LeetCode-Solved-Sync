class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers
        left = 0                  # Start pointer at the beginning of the list
        right = len(numbers) - 1  # End pointer at the end of the list

        # Loop until the two pointers meet
        while left < right:
            # Calculate the sum of the elements at the current pointers
            total = numbers[left] + numbers[right]

            # If the sum matches the target, return the indices (1-based)
            if total == target:
                return [left + 1, right + 1]

            # If the sum is greater than the target, move the right pointer left
            elif total > target:
                right -= 1

            # If the sum is less than the target, move the left pointer right
            else:
                left += 1
