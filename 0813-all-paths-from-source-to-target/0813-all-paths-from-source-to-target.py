class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res=[]
        n=len(graph)-1
        def dfs(i,path):
            if i==n:
                res.append(path)
            else:
                for j in graph[i]:
                    if j not in path :
                        dfs(j,path+[j])
        dfs(0,[0])
        return res
                