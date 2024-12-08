class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge case: if the list is empty, there is no common prefix
        if not strs:
            return ""
        
        # Step 1: Initialize the prefix with the shortest string in the list
        prefix = min(strs, key=len)  # This ensures the prefix cannot be longer than the shortest string
        
        # Step 2: Compare the prefix with each string in the list
        for s in strs:
            # Step 3: If the prefix doesn't match the start of the current string, reduce the prefix
            while not s.startswith(prefix):
                # Shorten the prefix by one character
                prefix = prefix[:-1]
                # If prefix becomes empty, no common prefix exists
                if not prefix:
                    return ""
        
        # Step 4: Return the longest common prefix
        return prefix
