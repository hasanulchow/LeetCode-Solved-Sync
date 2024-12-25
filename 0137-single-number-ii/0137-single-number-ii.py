from collections import defaultdict

class Solution:
    def singleNumber(self, nums):
        """
        Finds the element that appears exactly once in the given list of numbers, where every other element appears twice.

        Args:
        nums (list): The input list of integers where all elements except one appear twice.

        Returns:
        int: The element that appears only once.
        """
        # Initialize a defaultdict to count occurrences of each number
        count = defaultdict(int)
        
        # Count the frequency of each number in the input list
        for x in nums:
            count[x] += 1

        # Iterate through the dictionary to find the number that appears exactly once
        for x, freq in count.items():
            if freq == 1:
                return x
        
        # If no such number is found (though the problem guarantees one number appears once), return -1
        return -1
