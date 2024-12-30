class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        # Depth-First Search function to mark connected bricks
        def dfs(x, y):
            # Check for valid brick and bounds
            if not (0 <= x < m and 0 <= y < n) or grid[x][y] != 1:
                return 0
            # Mark the brick as visited to prevent cycles
            grid[x][y] = 2  
            # Count this brick and all connected bricks
            return 1 + sum(dfs(x + dx, y + dy) for dx, dy in dirs if 0 <= x + dx < m and 0 <= y + dy < n)
        
        # Function to check if a brick is stable
        def is_stable(x, y):
            # A brick is stable if it's in the top row or connected to a stable brick
            return x == 0 or any((0 <= nx < m and 0 <= ny < n) and grid[nx][ny] == 2 for nx, ny in [(x + dx, y + dy) for dx, dy in dirs])
        
        # Dimensions of the grid and possible move directions
        m, n, dirs = len(grid), len(grid[0]), [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Step 1: Simulate the hits and remove bricks
        for x, y in hits:
            if 0 <= x < m and 0 <= y < n: 
                grid[x][y] -= 1
        
        # Step 2: Perform DFS from the top row to find all stable bricks
        for y in range(n):
            dfs(0, y)
        
        # Step 3: Reverse the hits and for each hit, try to make the brick fall if it's unstable
        res = []
        for x, y in reversed(hits):
            if 0 <= x < m and 0 <= y < n:  
                grid[x][y] += 1
                # Only perform DFS if the current brick is stable
                res.append(dfs(x, y) - 1 if grid[x][y] == 1 and is_stable(x, y) else 0)
        
        # Return the result in the original hit order
        return res[::-1]