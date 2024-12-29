class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])

        # Remove lands connected to edge
        def dfs(A, i, j):
            if i < 0 or i == len(A) or j < 0 or j == len(A[0]):
                return
            if A[i][j] == 0:
                return

            A[i][j] = 0
            dfs(A, i + 1, j)
            dfs(A, i - 1, j)
            dfs(A, i, j + 1)
            dfs(A, i, j - 1)

        for i in range(m):
            for j in range(n):
                if i * j == 0 or i == m - 1 or j == n - 1:
                    if A[i][j] == 1:
                        dfs(A, i, j)

        ans = 0

        for row in A:
            ans += sum(row)

        return ans