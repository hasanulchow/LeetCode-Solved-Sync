from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        # Helper function to check if a substring is a palindrome
        def is_palindrome(sub):
            return sub == sub[::-1]  # Check if the string is equal to its reverse

        # Backtracking function to generate all palindromic partitions
        def backtrack(start, path):
            if start == len(s):  # Base case: if we have processed the entire string
                result.append(path[:])  # Add the current partition (path) to the result
                return
            for end in range(start + 1, len(s) + 1):  # Explore all possible substrings
                if is_palindrome(s[start:end]):  # Check if the substring is a palindrome
                    backtrack(end, path + [s[start:end]])  # Recurse with the new substring

        result = []  # List to store all palindromic partitions
        backtrack(0, [])  # Start backtracking from index 0 with an empty path
        return result  # Return the list of all valid palindromic partitions
