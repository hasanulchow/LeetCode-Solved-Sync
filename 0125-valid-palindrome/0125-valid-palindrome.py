class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Filter and normalize the input string
        # Convert the string to lowercase and keep only alphanumeric characters
        s = "".join(filter(str.isalnum, s.lower()))
        
        # Step 2: Check if the cleaned string is equal to its reverse
        return s == s[::-1]
