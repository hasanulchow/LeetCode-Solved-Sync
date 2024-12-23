class Solution {
public:
    //int calculateMinimumHP(vector<vector<int>>& dungeon) {
        //find max no. which will be -ve
        //hame max -ve no. nikalna hai
        //mtlb sabse chota dis
        //-ve no. found then return 1+(+ve of(-no.))
        
    //     int n=dungeon.size();
    //     int m=dungeon[0].size();
    //     int ans=INT_MAX;
    //     vector<vector<int>>dist(n,vector<int>(m,INT_MIN));//we have to store max health value
    //     dist[0][0]=dungeon[0][0];
    //     queue<pair<int,pair<int,int>>>q;///d r c
    //     q.push({dungeon[0][0],{0,0}});
    //     vector<pair<int,int>>dir={{0,1},{1,0}};
    //     int ans1=INT_MAX;
    //     int ans2=INT_MAX;
    //     while(!q.empty()){
    //         int d=q.front().first;
    //         int r=q.front().second.first;
    //         int c=q.front().second.second;
    //         q.pop();
    //         if(r==n-1 && c==m-1){
    //             ans=min(ans,d);
    //         }
    //         if(r==n-2 && c==m-1){
    //             ans1=min(ans1,d);
    //         }
    //         if(r==n-1 && c==m-2){
    //             ans2=min(ans2,d);
    //         }
    //         for(int i=0;i<2;i++){
    //             int newr=r+dir[i].first;
    //             int newc=c+dir[i].second;
    //             if(newr>=0 && newr<n && newc>=0 && newc<m && dist[newr][newc]<d+dungeon[newr][newc]){
    //                     dist[newr][newc]=d+dungeon[newr][newc];
    //                     q.push({dist[newr][newc],{newr,newc}});
    //             }
    //         }
    //     }
    //     if(ans>=0)return 1;
    //     else if(ans1<0 && ans1<ans2 && dist[n-1][m-1]>0) return -1*ans1+1;
    //     else if(ans2<0 && ans2<ans1 && dist[n-1][m-1]>0) return -1*ans2+1;
    //     return 1+ (-1*ans);
        
    // }
    //wrong ans
    /*
    Incorrect Dynamic Programming Approach: The problem is not about maximizing health but about ensuring the minimum amount of health required to survive at any given cell. Your approach is trying to maximize the health gained, which leads to incorrect calculations.

Priority Queue Not Needed: You are trying to solve this with a BFS-like approach, but the problem requires dynamic programming to track the minimum health needed to reach the bottom-right cell starting from the bottom-right and moving backward.

Misinterpretation of Conditions: The conditions like ans1 and ans2 are not relevant to this problem. The problem requires us to ensure that we always have positive health at every cell along the way from start to end.
    */

    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int n = dungeon.size();
        int m = dungeon[0].size();
        
        // DP table to store minimum health needed at each cell
        vector<vector<int>> dp(n, vector<int>(m, INT_MAX));
        
        // Base case: The knight must have at least 1 health point to enter the princess's room
        dp[n-1][m-1] = max(1, 1 - dungeon[n-1][m-1]);

        // Fill the last row (from bottom to top)
        for (int i = n - 2; i >= 0; --i) {
            dp[i][m-1] = max(1, dp[i+1][m-1] - dungeon[i][m-1]);
        }

        // Fill the last column (from right to left)
        for (int j = m - 2; j >= 0; --j) {
            dp[n-1][j] = max(1, dp[n-1][j+1] - dungeon[n-1][j]);
        }

        // Fill the rest of the table
        for (int i = n - 2; i >= 0; --i) {
            for (int j = m - 2; j >= 0; --j) {
                int down = max(1, dp[i+1][j] - dungeon[i][j]);
                int right = max(1, dp[i][j+1] - dungeon[i][j]);
                dp[i][j] = min(down, right);
            }
        }

        // The result is the minimum health needed at the starting point
        return dp[0][0];
    }

};