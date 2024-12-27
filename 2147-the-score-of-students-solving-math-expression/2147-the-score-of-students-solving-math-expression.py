class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        @lru_cache(None)
        def allEval(x):
            lo = eval(x)
            if lo > 1000:
                return set()
            ans = set([lo])
            if '*' not in x or '+' not in x or lo==1000:
                return ans
            for pos, char in enumerate(x):
                if char not in ['+', '*']:
                    continue
                left, right = allEval(x[:pos]), allEval(x[pos+1:])
                if char == '+':
                    ans |= {a + b for a in left for b in right if a+b<=1000}
                if char == '*':
                    ans |= {a * b for a in left for b in right if a*b<=1000}
            return ans
        S = allEval(s)
        correct = eval(s)
        return sum(5 if x==correct else (2 if x in S else 0) for x in answers)