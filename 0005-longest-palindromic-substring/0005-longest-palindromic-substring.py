class Solution:
    def longestPalindrome(self, s: str) -> str:
        candidates = {}  # Dictionary to store palindromic substrings and their lengths
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if substring == substring[::-1]:  # Check if the substring is a palindrome
                    candidates[substring] = len(substring)
        
        # Get the longest palindrome by length
        max_palindrome = max(candidates, key=candidates.get)
        return max_palindrome
