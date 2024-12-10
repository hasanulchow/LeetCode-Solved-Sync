class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.

        Args:
        s (str): The input string.

        Returns:
        int: The length of the longest substring without repeating characters.
        """
        max_length = 0  # Tracks the maximum length of substring found
        left = 0  # Sliding window left pointer
        count = {}  # Dictionary to store the count of characters in the current window

        for right, c in enumerate(s):  # Right pointer moves through the string
            count[c] = 1 + count.get(c, 0)  # Increment the count of the current character

            # If character count exceeds 1, shrink the window from the left
            while count[c] > 1:
                count[s[left]] -= 1  # Decrement the count of the leftmost character
                left += 1  # Move the left pointer to the right

            # Update the maximum length of the substring
            max_length = max(max_length, right - left + 1)

        return max_length
