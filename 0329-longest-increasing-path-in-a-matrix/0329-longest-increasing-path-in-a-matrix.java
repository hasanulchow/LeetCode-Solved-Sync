class Solution {
    int[][] matrix, helper;
    int[][] dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}}; // Directions: right, down, left, up

    public int longestIncreasingPath(int[][] matrix) {
        // Edge case: if the matrix is empty
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return 0;

        this.matrix = matrix;
        int m = matrix.length, n = matrix[0].length;

        // Memoization array to store the length of the longest path starting from each cell
        helper = new int[m][n];
        int path = 0;

        // Traverse each cell and compute the longest increasing path starting from it
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                path = Math.max(path, dfs(i, j));
            }
        }

        return path;
    }

    private int dfs(int x, int y) {
        // If already computed, return the cached value
        if (helper[x][y] != 0) return helper[x][y];

        // Explore all four directions
        for (int[] dir : dirs) {
            int i = x + dir[0], j = y + dir[1];
            // Check boundary conditions and if the next cell is greater than the current cell
            if (i >= 0 && i < matrix.length && j >= 0 && j < matrix[0].length && matrix[x][y] < matrix[i][j]) {
                helper[x][y] = Math.max(helper[x][y], dfs(i, j));
            }
        }

        // Increment the length for the current cell (counting itself)
        return ++helper[x][y];
    }
}
