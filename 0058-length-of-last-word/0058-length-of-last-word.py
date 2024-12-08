class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Step 1: Initialize `end` to the index of the last character of the string `s`
        end = len(s) - 1
        
        # Step 2: Skip any trailing spaces from the end of the string
        # This loop moves `end` backward until it finds a non-space character
        while end >= 0 and s[end] == " ":
            end -= 1

        # Step 3: Set `start` to the position of the last non-space character found
        start = end
        
        # Step 4: Move `start` backward until a space or the beginning of the string is found
        # This loop finds the beginning of the last word
        while start >= 0 and s[start] != " ":
            start -= 1
        
        # Step 5: Return the length of the last word by subtracting `start` from `end`
        # The length of the last word is the difference between `end` and `start`
        return end - start

        