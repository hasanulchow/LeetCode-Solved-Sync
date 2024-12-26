from collections import defaultdict
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = defaultdict(str)
        for c in 'abcdefghijklmnopqrstuvwxyz':
            parent[c] = c 
        def find(v):
            if parent[v] != v:
                parent[v] = find(parent[v])
            return parent[v]
        def union(v,w):
            pv, pw = find(v), find(w)
            if pv < pw:
                parent[pw] = pv
            else:
                parent[pv] = pw 
        for v, w in zip(s1, s2):
            union(v, w)
        res = []
        for c in baseStr:
            res.append(find(c))
        return "".join(res)