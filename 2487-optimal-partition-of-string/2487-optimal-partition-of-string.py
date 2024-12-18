class Solution:
    def partitionString(self, s: str) -> int:
        """
        Splits the input string `s` into the minimum number of substrings
        such that each substring contains unique characters.

        :param s: str - The input string to be partitioned.
        :return: int - The number of substrings created.
        """
        # Initialize the count of substrings to 1 (at least one substring exists).
        ans = 1
        
        # List to store characters of the current substring.
        ls = []

        # Iterate through each character in the string.
        for i in s:
            # If the character is already in the current substring,
            # start a new substring and increment the counter.
            if i in ls:
                ls = [i]  # Reset the list with the current character.
                ans += 1
            else:
                # Otherwise, add the character to the current substring.
                ls += [i]

        # Return the total number of substrings created.
        return ans
