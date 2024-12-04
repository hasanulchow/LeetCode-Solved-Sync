class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, j = 0, 0

        while i < len(str1) and j < len(str2):
            # Check if characters match directly
            if str1[i] == str2[j]:
                j += 1
            # Check if a character in str1 can be transformed to match str2[j]
            elif chr((ord(str1[i]) - ord('a') + 1) % 26 + ord('a')) == str2[j]:
                j += 1
            i += 1

        # If we've iterated through all characters of str2, it's a valid subsequence
        return j == len(str2)
