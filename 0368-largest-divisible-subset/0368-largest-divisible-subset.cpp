class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        const int n = nums.size();
        vector<int> deg(n, 0), prev(n, -1);
        vector<vector<int>> adj(n);

        //Kahn's algo
        for (int i = 0; i < n; i++) {//Build adjacent list
            for (int j = i+1; j < n; j++) {
                if (nums[j] % nums[i] == 0) {
                    adj[i].push_back(j);
                    deg[j]++;//indegree
                }
            }
        }
        // BSF
        queue<int> q;
        for (int i = 0; i < n; i++) {
            if (deg[i]==0) q.push(i);
        }

        int iMax= 0;
        while (!q.empty()) {
            int x=q.front();
            q.pop();
            for (int y : adj[x]) {
                if (--deg[y] == 0) {
                    q.push(y);
                    prev[y]=x;//assign prev
                }
            }
            iMax=x;
        }
        vector<int> ans;
        for (int j=iMax; j!=-1; j=prev[j]) {
            ans.push_back(nums[j]);
        }
        return ans;
    }
};
