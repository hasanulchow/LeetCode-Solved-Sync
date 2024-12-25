class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)
        p, n = int(n[:(l+1)//2]), int(n)
        candidates = {10**(l-1)-1, 10**l+1, *(int((t:=str(p+q)) + t[-1-l%2::-1]) for q in (-1,0,1))} - {n}
        
        return str(min(candidates, key=lambda v: (abs(v-n),v)))