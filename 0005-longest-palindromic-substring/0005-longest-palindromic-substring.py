class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Finds the longest palindromic substring in a given string.

        Args:
        s (str): The input string.

        Returns:
        str: The longest palindromic substring.
        """
        # If the string length is 1 or less, it is already a palindrome.
        if len(s) <= 1:
            return s
        
        Max_Len = 1  # The length of the longest palindrome found.
        Max_Str = s[0]  # The longest palindrome found, initially the first character.

        # Iterate through all possible substrings.
        for i in range(len(s) - 1):  # Outer loop to define the starting point of the substring.
            for j in range(i + 1, len(s)):  # Inner loop to define the ending point of the substring.
                # Check if the length of the current substring is greater than the current maximum length
                # and if the substring is a palindrome.
                if j - i + 1 > Max_Len and s[i:j + 1] == s[i:j + 1][::-1]:
                    Max_Len = j - i + 1  # Update the maximum length.
                    Max_Str = s[i:j + 1]  # Update the longest palindrome string.

        return Max_Str  # Return the longest palindrome substring.
