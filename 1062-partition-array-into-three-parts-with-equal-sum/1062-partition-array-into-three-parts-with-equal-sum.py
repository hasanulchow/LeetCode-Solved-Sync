class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
    	S = sum(A)
    	if S % 3 != 0: return False
    	g, C, p = S//3, 0, 0
    	for a in A[:-1]:
    		C += a
    		if C == g:
    			if p == 1: return True
    			C, p = 0, 1
    	return False