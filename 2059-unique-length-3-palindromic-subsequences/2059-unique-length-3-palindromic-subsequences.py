class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [float('inf')] * 26
        last = [-1] * 26
        result = 0

        for i, char in enumerate(s):
            first[ord(char) - ord('a')] = min(first[ord(char) - ord('a')], i)
            last[ord(char) - ord('a')] = i

        for i in range(26):
            if first[i] < last[i]:
                result += len(set(s[first[i] + 1:last[i]]))

        return result