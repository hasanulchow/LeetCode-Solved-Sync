class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        highrows = [0]*len(grid)
        highcols = [0]*len(grid[0])

        totalsum, n = 0, 0

        for i in range(len(grid)):
            highrows[i] = max(grid[i])
            n += sum(grid[i])
            for j in range(len(grid[0])):
                if highcols[j] < grid[i][j]:
                    highcols[j] = grid[i][j]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
               totalsum += min(highrows[i], highcols[j]) 

        return totalsum - n