from collections import Counter

class Solution:
    def maximumLength(self, s: str) -> int:
        """
        Finds the maximum length of substrings that occur at least 3 times in the input string.
        
        Args:
        s (str): Input string.
        
        Returns:
        int: Maximum length of such substrings, or -1 if no substring occurs at least 3 times.
        """
        # List to store all possible substrings
        subarrays = []
        
        # Generate substrings with the same consecutive characters
        for i in range(len(s)):
            index = i
            while index < len(s) and s[index] == s[i]:
                # Add substring of repeated characters to the list
                subarrays.append(s[i:index + 1])
                index += 1
        
        # Count occurrences of each substring
        counter = Counter(subarrays)
        max_len = 0

        # Check for substrings that appear at least 3 times
        for substring, count in counter.items():
            if count >= 3:
                # Update the maximum length if the current substring is longer
                max_len = max(max_len, len(substring))

        # If no substring meets the criteria, return -1
        if max_len == 0:
            return -1

        return max_len
