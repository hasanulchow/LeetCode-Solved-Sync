class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        now = maximumHeight[0]
        sum = 0
        n = len(maximumHeight)
        for i in range(n):
            now = min(now, maximumHeight[i])
            if now<=0:
                return -1
            sum +=now  
            now-=1
            
        return sum