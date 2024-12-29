class Solution:
	def uniquePathsIII(self, grid: List[List[int]]) -> int:

		def DFS(row, col, count_zero, grid):

			if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == -1:
				return 0

			if grid[row][col] == 2:
				if count_zero == -1:
					return 1
				else:
					return 0

			grid[row][col] = -1

			count_zero = count_zero - 1

			total_paths = DFS(row + 1, col, count_zero, grid) + DFS(row, col + 1, count_zero, grid) + DFS(row - 1, col, count_zero, grid) + DFS(row, col - 1, count_zero, grid)

			grid[row][col] = 0

			count_zero = count_zero + 1

			return total_paths

		count_zero = 0
		x,y = 0,0

		for r in range(len(grid)):
			for c in range(len(grid[0])):

				if grid[r][c] == 0:
					count_zero = count_zero + 1

				elif grid[r][c] == 1:
					x,y = r,c

		return DFS(x, y, count_zero, grid)