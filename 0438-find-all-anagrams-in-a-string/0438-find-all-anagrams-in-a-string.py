from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        ans = []  # List to store the starting indices of anagrams of `p` in `s`
        count = Counter(p)  # Counter to track the frequency of characters in `p`
        required = len(p)  # Variable to keep track of how many characters are still required to match the anagram

        # Iterate over each character in `s`
        for r, c in enumerate(s):
            # Decrease the count of the current character `c` in the window
            count[c] -= 1
            
            # If the character `c` is still part of a valid anagram, decrease the required count
            if count[c] >= 0:
                required -= 1

            # If the window size exceeds the length of `p`, slide the window
            if r >= len(p):
                # Move the left side of the window by increasing the count of the character that is leaving
                left_char = s[r - len(p)]
                count[left_char] += 1
                # If this character was previously required, increment the required count
                if count[left_char] > 0:
                    required += 1

            # If no characters are required, we have found an anagram, so add the starting index to the result
            if required == 0:
                ans.append(r - len(p) + 1)

        return ans  # Return the list of starting indices of anagrams of `p` in `s`
