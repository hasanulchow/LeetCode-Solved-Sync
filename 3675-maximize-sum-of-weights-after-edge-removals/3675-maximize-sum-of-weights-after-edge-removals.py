class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        graph = {}
        for a, b, w in edges:
            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}
            graph[a][b] = graph[b][a] = w
        
        @cache
        def solve(root, has_par, par):
            # print(root, has_par, par)
            costs = []
            for ch in graph[root]:
                if ch == par:
                    continue
                pick = graph[root][ch] + solve(ch, 1, root)
                nopick = solve(ch, 0, root)
                costs.append((pick - nopick, ch))
            costs.sort(key = lambda t : t[0], reverse=True)
            # print('costs=', costs)
            picked = 0
            res = 0
            cur_k = k - has_par
            for c, ch in costs:
                if c > 0 and picked < cur_k:
                    res += graph[root][ch] + solve(ch, 1, root)
                    picked += 1
                else:
                    res += solve(ch, 0, root)
                
            return res
            
                    
        
        return solve(0, 0, None)