class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        fruits.sort()    # sort for later binary search
        res = 0
        dic = {}           #index: prefix sum
        cur = 0
        for i,v in enumerate(fruits):
            cur += v[1]
            dic[i] = cur    # build prefix sum dictionary
        def go(i):   # input index i and this helper function means we start from startPos and make a turn at index i 
            if i < startPos:
                l = max(startPos - k,i)
                r = max(k - (startPos - l) + l,startPos)
            else:
                r = min(startPos + k,i)
                l = min(startPos,startPos - max(0,(k - (r - startPos) * 2)))
            li = bisect_left(fruits,[l,0])
            ri = bisect_right(fruits,[r,10 ** 20])  #binary search to get the boundarys in sorted fruits list, indicate the fruits in this boundary are reachable in k steps
            rval = dic[ri - 1] if ri - 1 >= 0 else 0
            lval = dic[li - 1] if li - 1 >= 0 else 0  #use the prefix sum dictionary we created to avoid extra O(n) complexity in helper function
            return rval - lval
            
        
        for i in range(n):
            
            res = max(go(fruits[i][0]),res)
        return res