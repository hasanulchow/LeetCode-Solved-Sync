class Solution {
    public int countCompleteComponents(int n, int[][] edges) {
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for(int i=0;i<n;i++) adj.add(new ArrayList<>());
        for(int edge[]:edges)
        {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }
        int ans =0;
        boolean visited[] = new boolean[n];
        for(int i=0;i<n;i++)
        {
            if(!visited[i])
            {
                int ne[] = {0,0};
                bfs(i,adj,visited,ne);
                if(ne[0]*(ne[0]-1)/2 == ne[1]/2)
                {
                    ans++;
                }
            }
        }
        return ans;        
    }
    private void bfs(int i,ArrayList<ArrayList<Integer>> adj,boolean visited[],int ne[])
    {
       Queue<Integer>  q = new LinkedList<>();
       q.add(i);
       visited[i] = true;
       while(!q.isEmpty())
       {
        int curr = q.poll();
        ne[0]++;
        
        for(int num:adj.get(curr))
        {
            ne[1]++;
            if(!visited[num])
            {
                q.offer(num);
                visited[num] = true;
                
            }
        }
       }
    }
}