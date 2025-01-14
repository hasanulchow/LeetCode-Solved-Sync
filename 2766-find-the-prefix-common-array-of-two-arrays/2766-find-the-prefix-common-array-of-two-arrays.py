class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)
        ans=[0]*n
        seen, count=0, 0
        for i in range(n):
            a, b=A[i], B[i]
            seen|=1<<(2*a-1)
            if seen& 1<<(2*a): count+=1
            seen|=1<<(2*b)
            if seen& 1<<(2*b-1): count+=1
            ans[i]=count
        return ans
        