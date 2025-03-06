class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        list: List[int]=[]
        n=len(grid)
        arr: list[int]=[0]*(n*n+1)

        for i in range(0, n):
            for j in range(0, n):
                arr[grid[i][j]]+=1
        
        for i in range(1, n*n+1):
            if arr[i]>1:
                list.insert(0, i)
            if arr[i]==0:
                list.insert(1, i)

        return list