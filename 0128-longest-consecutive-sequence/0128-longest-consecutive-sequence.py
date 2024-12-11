class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Initialize the variable to store the longest streak
        longest = 0
        
        # Convert the list to a set for O(1) lookups
        num_set = set(nums)

        # Iterate through each number in the set
        for n in num_set:
            # Check if the current number is the start of a sequence
            # (i.e., n-1 is not in the set)
            if (n - 1) not in num_set:
                # Initialize the current sequence length
                length = 1
                
                # Increment the length while the next number in the sequence exists
                while (n + length) in num_set:
                    length += 1
                
                # Update the longest sequence length if the current is longer
                longest = max(longest, length)

        # Return the longest consecutive sequence length
        return longest
