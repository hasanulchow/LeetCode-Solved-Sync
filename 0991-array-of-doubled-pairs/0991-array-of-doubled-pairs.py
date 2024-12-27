class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        c = Counter(A)
        for n in sorted(c.keys(), key=abs):
            while c[n] > 0 and c[(double := 2 * n)] > 0:
                c[n] -= 1
                c[double] -= 1
        return all(not v for v in c.values())