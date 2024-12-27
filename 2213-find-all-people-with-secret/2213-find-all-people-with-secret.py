class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        g={i:[] for i in range(n)}
        for (src,dst,wt) in meetings: 
            g[src].append((dst,wt))
            g[dst].append((src,wt))
            
        q=[(0,0),(firstPerson,0)]
        v={}
        while q:
            node,time=q.pop(0)
            if node in v and v[node]<=time: continue
            v[node]=time
            for (n,t) in g[node]:
                if t<time or (n in v and v[n]<=t):continue
                q.append((n,t))
        return list(v)