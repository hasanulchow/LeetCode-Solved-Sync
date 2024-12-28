from typing import List

class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        n = len(s)
        next = [0] * 26
        prev = [0] * 26
        
        for i in range(26):
            next[i] = nextCost[i]
            prev[i] = previousCost[i]
        
        # Calculate cumulative costs for next and previous
        for i in range(1, 26):
            next[i] += next[i - 1]
        for i in range(24, -1, -1):
            prev[i] += prev[i + 1]
        
        cost = 0
        for i in range(n):
            if s[i] != t[i]:
                start = ord(s[i]) - ord('a')
                end = ord(t[i]) - ord('a')
                
                if start < end: # case 1
                    forwardCost = next[end - 1] - (next[start - 1] if start > 0 else 0)
                    backwardCost = prev[0] - (prev[start + 1] if start + 1 < 26 else 0) + (0 if end == 25 else prev[end + 1])
                    cost += min(forwardCost, backwardCost)
                else: # case 2
                    backwardCost = prev[end + 1] - (0 if start >= 25 else prev[start + 1])
                    forwardCost = next[25] - next[start - 1] + (next[end - 1] if end != 0 else 0)
                    cost += min(forwardCost, backwardCost)
        
        return cost