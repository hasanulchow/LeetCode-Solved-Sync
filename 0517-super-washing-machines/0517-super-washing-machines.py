class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        if total % len(machines): return -1 # impossible 
        avg = total // len(machines)
        
        ans = prefix = 0
        for i, x in enumerate(machines): 
            ans = max(ans, abs(prefix), x - avg)
            prefix += x - avg
        return ans 