class Solution:
    def dfs(self, adjacency_list, visited, parent, node, tin, low, ans):
        visited[node] = 1
        tin[node] = tin[parent] + 1 if parent != -1 else 1
        low[node] = tin[node]

        for neighbor in adjacency_list[node]:
            if neighbor == parent:
                continue
            if not visited[neighbor]:
                self.dfs(adjacency_list, visited, node, neighbor, tin, low, ans)
                low[node] = min(low[node], low[neighbor])

                if low[neighbor] > tin[node]:
                    # bridge found
                    ans.append((neighbor, node))
            else:
                low[node] = min(low[node], low[neighbor])

    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        # bridges in graph implementation
        visited = [0] * n
        tin = [0] * n
        low = [0] * n
        adjacency_list = [[] for _ in range(n)]
        ans = []

        for u, v in connections:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)

        self.dfs(adjacency_list, visited, -1, 0, tin, low, ans)

        return ans