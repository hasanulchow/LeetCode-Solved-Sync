class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        m_graph = defaultdict(list)
        for i, man in enumerate(manager):
            m_graph[man].append(i)
        def dfs(i,temp):
            temp += informTime[i]
            if temp>self.ans:
                self.ans = temp
            for j in m_graph[i]:
                dfs(j,temp)
        self.ans = 0
        dfs(headID,0)
        return self.ans