class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n=len(pattern)
        d=[0]*n
        d[-1]+=(pattern[-1]=='D')
        for i in range(n-2, -1, -1):
            d[i]=d[i+1]+1 if pattern[i]=='D' else 0
        ans=[ chr(i+ord('1')) for i in range(n+1)]
        i=0
        while i<n:
            if pattern[i]=='D':
                l, r=i, i+d[i]
                while l<r:
                    ans[l], ans[r]=ans[r], ans[l]
                    l+=1
                    r-=1
            i+=d[i]+1
        return "".join(ans)
        