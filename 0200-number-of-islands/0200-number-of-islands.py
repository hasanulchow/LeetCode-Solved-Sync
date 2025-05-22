class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        count = 0

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] =='0':
                return
            grid[row][col] = '0'

            dfs(row -1, col)
            dfs(row +1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    dfs(row, col)
                    count += 1
        return count


    





            
        