import copy

class Solution:
    def countPyramids(self, grid):
        def in_range(i, j):
            return 0 <= i < R and 0 <= j < C
        
        #count the total number of pyramids. 
        #Note that dp[i][j] == 1 means it's a cell of only one fertile land, so we don't want to count them
        def get_sum(dp):
            res = 0
            for i in range(R):
                for j in range(C):
                    if dp[i][j] >= 2:
                        res += dp[i][j] - 1
            return res
        
        R, C = len(grid), len(grid[0])
        
        #count the number of pyramidal plot
        dp = copy.deepcopy(grid)
        for i in range(R - 1, -1, -1):
            for j in range(C - 1, -1, -1):
                if grid[i][j] == 1:
                    val1 = dp[i + 1][j + 1] if in_range(i + 1, j + 1) else 0
                    val2 = dp[i + 1][j - 1] if in_range(i + 1, j - 1) else 0
                    dp[i][j] = min(val1, val2) + 1 if in_range(i + 1, j) and grid[i + 1][j] == 1 else 1
        
        #count the number of inverse pyramidal plot
        dp_inv = copy.deepcopy(grid)
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    val1 = dp_inv[i - 1][j + 1] if in_range(i - 1, j + 1) else 0
                    val2 = dp_inv[i - 1][j - 1] if in_range(i - 1, j - 1) else 0
                    dp_inv[i][j] = min(val1, val2) + 1 if in_range(i - 1, j) and grid[i - 1][j] == 1 else 1
        
        return get_sum(dp) + get_sum(dp_inv)