class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        
        onGrid = lambda x, y: 0 <= x < n and 0 <= y < m
        n, m, dx, dy = len(moveTime), len(moveTime[0]), 1, 0
        heap = [(0, 0, 0, 1)]
        seen = {(0,0)}

        while heap:
            time, x, y, step = heappop(heap)

            if (x, y) == (n - 1, m - 1): return time

            for _ in range(4):

                X, Y, dx, dy = x + dx, y + dy, -dy, dx

                if onGrid(X, Y) and (X, Y) not in seen:
                    t = max(time, moveTime[X][Y]) + step
                    heappush(heap, [t, X, Y, 3 - step])
                    seen.add((X, Y))