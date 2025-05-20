class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()

        left = 0

        maximum_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1

            char_set.add(s[right])

            maximum_length = max(maximum_length, right-left+1)

        return maximum_length