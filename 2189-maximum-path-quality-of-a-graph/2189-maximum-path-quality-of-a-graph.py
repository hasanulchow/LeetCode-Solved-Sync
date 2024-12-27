class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        ans = 0
        graph = collections.defaultdict(dict)
        for u, v, t in edges:
            graph[u][v] = t
            graph[v][u] = t
        
        def dfs(curr, visited, score, cost):
            if curr == 0:
                nonlocal ans
                ans = max(ans, score)
            
            for nxt, time in graph[curr].items():
                if time <= cost:
                    dfs(nxt, visited|set([nxt]), score+values[nxt]*(nxt not in visited), cost-time)
        
        dfs(0, set([0]), values[0], maxTime)
        return ans