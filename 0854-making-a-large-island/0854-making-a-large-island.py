class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def find_val(ref, grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0 or grid[i][j] == ref:
                return 0
            grid[i][j] = ref
            return 1 + (find_val(ref, grid, i+1, j) + find_val(ref, grid, i-1, j) + find_val(ref, grid, i, j+1) + find_val(ref, grid, i, j-1))

        n = len(grid)
        ref = 2
        max_area = -1
        mp = {}

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    k = find_val(ref, grid, i, j)
                    mp[ref] = k
                    ref += 1
                    max_area = max(max_area, k)

        mp[0] = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    sum_area = 0
                    seen = set()
                    if i > 0:
                        seen.add(grid[i-1][j])
                    if j > 0:
                        seen.add(grid[i][j-1])
                    if i < n-1:
                        seen.add(grid[i+1][j])
                    if j < n-1:
                        seen.add(grid[i][j+1])
                    for k in seen:
                        sum_area += mp.get(k, 0)
                    max_area = max(max_area, sum_area + 1)

        return max_area