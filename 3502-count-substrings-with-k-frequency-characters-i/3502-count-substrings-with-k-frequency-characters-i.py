class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        state = Counter()
        result = l = 0
        for r, char in enumerate(s):
            state[char] += 1
            while state[char] == k:
                result += n - r
                state[s[l]] -= 1
                l += 1
        return result