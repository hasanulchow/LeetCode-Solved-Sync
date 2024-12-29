class Solution:
    def subarraysDivByK(self, n: List[int], k: int) -> int:
        c=Counter([s:=(o:=0)])
        for v in n:
            s=(s+v)%k
            o+=c[s]
            c[s]+=1
        return o