class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Initialize dictionaries to store the first occurrence index of characters in both strings
        char_index_s = {}
        char_index_t = {}

        # Iterate through each character of the strings by index
        for i in range(len(s)):
            # If the character in `s` is not already in the dictionary, record its index
            if s[i] not in char_index_s:
                char_index_s[s[i]] = i
            
            # If the character in `t` is not already in the dictionary, record its index
            if t[i] not in char_index_t:
                char_index_t[t[i]] = i

            # Compare the indices of the current characters from `s` and `t`
            # If they differ, the strings are not isomorphic
            if char_index_s[s[i]] != char_index_t[t[i]]:
                return False

        # If all characters match in their index mappings, the strings are isomorphic
        return True
