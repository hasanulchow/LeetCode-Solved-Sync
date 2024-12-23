class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        // Check if the dungeon grid is null or empty, in which case return 1 (minimum HP to start).
        if(dungeon == null || dungeon.length == 0 || dungeon[0].length == 0) return 1;
        
        int N = dungeon.length; // Number of rows in the dungeon.
        int M = dungeon[0].length; // Number of columns in the dungeon.
        
        // Initialize the DP table (2D array) to store the minimum HP required at each position.
        int[][] dp = new int[N][M];
        
        // Base case: the minimum HP needed at the princess's room (bottom-right corner) should be 1.
        // If dungeon[N-1][M-1] is positive, we subtract it from 1; if it's negative, we adjust HP accordingly.
        dp[N - 1][M - 1] = 1 - dungeon[N - 1][M - 1];
        dp[N - 1][M - 1] = dp[N - 1][M - 1] <= 0 ? 1 : dp[N - 1][M - 1];  // Ensure at least 1 HP is needed.

        // Traverse the dungeon grid from bottom-right to top-left.
        for(int i = N - 1; i >= 0; --i){ // Loop through rows.
            for(int j = M - 1; j >= 0; --j){ // Loop through columns.
                if(i == N - 1 && j == M - 1) continue; // Skip the princess's room, already initialized.

                // Calculate the minimum HP required to reach the bottom or right cell.
                // HP_D: HP needed if moving down, or Integer.MAX_VALUE if out of bounds.
                // HP_R: HP needed if moving right, or Integer.MAX_VALUE if out of bounds.
                int HP_D = (i + 1 == N) ? Integer.MAX_VALUE : dp[i + 1][j] - dungeon[i][j];
                int HP_R = (j + 1 == M) ? Integer.MAX_VALUE : dp[i][j + 1] - dungeon[i][j];
                
                // The minimum HP required at position (i, j) is the minimum between HP_D and HP_R.
                int HP = Math.min(HP_D, HP_R);
                
                // Ensure that HP is at least 1, meaning the player will have at least 1 HP to move forward.
                dp[i][j] = HP <= 0 ? 1 : HP;
            }    
        }
        
        // Return the minimum HP required to reach the princess starting from the top-left corner.
        return dp[0][0];
    }
}
