class Solution:
    def dfs(self, adj: List[List[Tuple[int, int]]], visited: List[bool], minChange: List[int], currCity: int) -> None:
        visited[currCity] = True  # Mark the current city as visited
        
        # Explore all neighbors of the current city
        for neighbourCity in adj[currCity]:
            if not visited[neighbourCity[0]]:  # If the neighboring city hasn't been visited
                # If the direction of the road needs to be changed, increment minChange
                if neighbourCity[1] == 1:
                    minChange[0] += 1
                # Recursively visit the neighboring city
                self.dfs(adj, visited, minChange, neighbourCity[0])

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]  # Initialize adjacency list for n cities
        
        # Build the adjacency list where each city has its neighbors and the direction of the road
        for connection in connections:
            adj[connection[0]].append((connection[1], 1))  # Road from connection[0] to connection[1] (1 means direction)
            adj[connection[1]].append((connection[0], -1))  # Road from connection[1] to connection[0] (-1 means opposite direction)
        
        visited = [False] * n  # List to track visited cities
        minChange = [0]  # This will store the count of roads that need to be reversed
        
        self.dfs(adj, visited, minChange, 0)  # Start DFS from city 0
        
        return minChange[0]  # Return the minimum number of roads that need to be reordered
