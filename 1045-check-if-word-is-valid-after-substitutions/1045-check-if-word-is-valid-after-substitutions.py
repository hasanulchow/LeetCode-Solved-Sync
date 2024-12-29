class Solution:
    def isValid(self, s: str) -> bool:
        while("abc" in s): 
            s = s.replace("abc","") # continuously replace "abc" by "". By the end if we end up with "", then the word is valid.
        return s == ""