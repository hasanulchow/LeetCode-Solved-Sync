class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Step 1: Initialize the visited list to keep track of visited cities
        v = [False] * len(isConnected)  # v[i] will be True if city i is visited
        
        # Step 2: Define a DFS function to explore all cities connected to city i
        def dfs(i):
            # Explore all cities connected to city i
            for j in range(len(isConnected)):
                # If there is a connection and city j is not visited, visit it
                if isConnected[i][j] == 1 and not v[j]:
                    v[j] = True  # Mark city j as visited
                    dfs(j)  # Recursively visit all connected cities to j

        # Step 3: Count the number of provinces
        ans = 0
        for i in range(len(isConnected)):
            # If city i is not visited, it means it's a new province
            if not v[i]:
                dfs(i)  # Visit all cities connected to i
                ans += 1  # Increment the number of provinces

        # Step 4: Return the total number of provinces
        return ans
