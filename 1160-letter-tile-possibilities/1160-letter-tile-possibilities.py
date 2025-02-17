class Solution:
    def numTilePossibilities(self, s: str) -> int:
        d = Counter(s)
        res = 0
        def backtrack(sol):
            nonlocal res           
            if sol: 
                res += 1

            for i in d:
                if d[i] != 0:
                    d[i] -= 1
                    backtrack(sol + i)
                    d[i] += 1
                    
        backtrack("")
        return res