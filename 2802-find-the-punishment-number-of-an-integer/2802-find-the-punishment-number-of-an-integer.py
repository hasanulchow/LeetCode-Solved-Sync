class Solution:
    def punishmentNumber(self, n: int) -> int:
        @cache
        def rec(num):
            s = set()
            for i in range(len(num)):
                ops = rec(num[i+1:]) if num[i+1:] else set([0])
                for op in ops:
                    s.add(op + int(num[:i+1]))
            return s

        res = 0
        for i in range(1, n + 1):            
            if i in rec(str(i * i)):
                res += i * i
        return res