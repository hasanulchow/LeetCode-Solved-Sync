class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        N = len(s)

        if k == 0:
            return 0
        if N < max(3, k * 3):
            return -1

        count = {
            'a': 0,
            'b': 0,
            'c': 0
        }

        for c in s:
            count[c] += 1

        for freq in count.values():
            if freq < k:
                return -1

        res = N
        l = r = 0

        for l in range(N):
            while r < N and count[s[r]] > k:
                count[s[r]] -= 1
                r += 1
            
            res = min(res, N - r + l)
            
            count[s[l]] += 1
        
        return res