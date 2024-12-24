class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        temp = [(capital[i], profits[i]) for i in range(n)]
        temp.sort()

        maxHeap = []
        j = 0

        while k > 0:
            while j < n and w >= temp[j][0]:
                heapq.heappush(maxHeap, -temp[j][1])
                j += 1
            
            if not maxHeap:
                break
            
            w -= heapq.heappop(maxHeap)
            k -= 1
        
        return w