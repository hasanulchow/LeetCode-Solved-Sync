class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Step 1: Edge case check
        # If the length of the haystack is smaller than the needle, needle cannot be found
        if len(haystack) < len(needle):
            return -1  # Return -1 to indicate needle is not in haystack

        # Step 2: Iterate through the haystack to find the needle
        for i in range(len(haystack)):
            # Check if the substring starting at index i matches the needle
            if haystack[i:i + len(needle)] == needle:
                return i  # Return the starting index if a match is found

        # Step 3: If no match is found, return -1
        return -1
