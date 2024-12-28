class Solution:
    def maxGoodNumber(self, A):
        return (lambda a: max(int(''.join(c), 2) for c in permutations(a, 3)))(map(lambda s:s[2:],map(bin, A)))
        