class Solution:
    def numTilings(self, n: int) -> int:

        @cache
        def traverse(c, s):
            res = 0
            if c == n:
                return s == 0

            if s == 1:
                for state in [2,3]:
                    res += traverse(c+1, state)
            
            elif s == 2:
                for state in [1,3]:
                    res += traverse(c+1, state)
            elif s == 3:
                res += traverse(c+1, 0)
            elif s == 0:
                for state in [0,1,2,3]:
                    res += traverse(c+1, state)

            return res

        return traverse(0,0)%(10**9 + 7)
        
        