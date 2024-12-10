from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Finds the minimum window substring in `s` that contains all characters in `t`.
        
        Args:
        s (str): Input string to search.
        t (str): Target string whose characters need to be included in the window.
        
        Returns:
        str: The minimum window substring or an empty string if no valid window exists.
        """
        if not s or not t:
            return ""

        # Frequency count of characters in `t`
        count = Counter(t)
        required = len(t)  # Total characters in `t` to be matched
        bestLeft = -1
        minLength = len(s) + 1  # Initialize with a large number

        l = 0  # Left pointer of the sliding window
        for r, c in enumerate(s):  # Right pointer of the sliding window
            count[c] -= 1
            if count[c] >= 0:
                required -= 1

            # Try to shrink the window when all required characters are matched
            while required == 0:
                if r - l + 1 < minLength:
                    bestLeft = l
                    minLength = r - l + 1

                # Remove the leftmost character from the window
                count[s[l]] += 1
                if count[s[l]] > 0:
                    required += 1
                l += 1

        # Return the minimum window substring, or an empty string if no valid window
        return "" if bestLeft == -1 else s[bestLeft: bestLeft + minLength]
