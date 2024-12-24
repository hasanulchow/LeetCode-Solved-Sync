class Solution {
    public int maxSumSubmatrix(int[][] matrix, int k) {
        final int rows = matrix.length;
        final int cols = matrix[0].length;
        final int[][] prefixSum = new int[rows + 1][cols + 1];

        // Build prefix sum array
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                prefixSum[r + 1][c + 1] = prefixSum[r][c + 1] + prefixSum[r + 1][c] - prefixSum[r][c] + matrix[r][c];
            }
        }

        int max = Integer.MIN_VALUE;

        // Explore all submatrices
        for (int rowSize = 0; rowSize < rows; rowSize++) {
            for (int colSize = 0; colSize < cols; colSize++) {
                for (int rStart = 0; rStart + rowSize < rows; rStart++) {
                    for (int cStart = 0; cStart + colSize < cols; cStart++) {
                        final int r1 = rStart;
                        final int c1 = cStart;
                        final int r2 = rStart + rowSize;
                        final int c2 = cStart + colSize;
                        final int sum = prefixSum[r2 + 1][c2 + 1] + prefixSum[r1][c1] - prefixSum[r1][c2 + 1] - prefixSum[r2 + 1][c1];

                        if (sum == k) return k;
                        else if (sum < k) max = Math.max(max, sum);
                    }
                }
            }
        }

        return max;
    }
}
