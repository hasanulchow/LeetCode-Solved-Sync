class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        deque_ = deque([(0,0,0)])
        visited = [[False]*n for _ in range(m)]
        visited[0][0] = True

        while deque_:
            x,y, obstacles_removed = deque_.popleft()

            if x== m-1 and y == n-1:
                return obstacles_removed

            for dx,dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if grid[nx][ny] == 0:
                        deque_.appendleft((nx, ny, obstacles_removed))
                    else:
                        deque_.append((nx, ny, obstacles_removed + 1))

        return -1
        