class Solution:
    def countWinningSequences(self, s: str) -> int:
        def fight(a, b):
            if a == "F":
                if b == "E":
                    return 1
                elif b == "W":
                    return -1
            elif a == "W":
                if b == "F":
                    return 1
                elif b == "E":
                    return -1
            else:
                if b == "W":
                    return 1
                elif b == "F":
                    return -1
            return 0

        @cache
        def dp(i, prev, point):
            if i == len(s):
                return int(point > 0)
            res = 0
            for c in "FWE":
                if c == prev:
                    continue
                res += dp(i + 1, c, point + fight(c, s[i]))
                res %= 1_000_000_007
            return res
        
        return dp(0, '', 0)