class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort the characters of the first string `s` and store the result
        sorted_s = sorted(s)
        
        # Sort the characters of the second string `t` and store the result
        sorted_t = sorted(t)
        
        # Compare the sorted versions of the two strings
        # If they are identical, `s` and `t` are anagrams; otherwise, they are not
        return sorted_s == sorted_t
