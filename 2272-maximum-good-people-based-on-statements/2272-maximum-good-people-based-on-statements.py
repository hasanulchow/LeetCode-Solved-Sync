class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        hm_good = {i: set([i]) for i in range(n)}
        hm_bad = {i: set() for i in range(n)}
        for i in range(n):
            for j in range(n):
                if statements[i][j] == 0:
                    hm_bad[i].add(j)
                elif statements[i][j] == 1:
                    hm_good[i].add(j)
        def helper(i, good, bad):
            if i == n:
                return len(good) if not good.intersection(bad) else -1
            if i in bad:
                return helper(i+1, good, bad)
            if hm_good[i].intersection(bad) or hm_bad[i].intersection(good):
                if i in good:
                    return -1
                return helper(i+1, good, bad.union(set([i])))
            return max(helper(i+1, good, bad.union(set([i]))), \
            helper(i+1, good.union(hm_good[i]), bad.union(hm_bad[i])))
        return helper(0, set(), set())