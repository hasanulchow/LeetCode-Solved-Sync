class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        
        def fn(sub): 
            """Return ops to make sub non-decreasing."""
            vals = []
            for x in sub: 
                k = bisect_right(vals, x)
                if k == len(vals): vals.append(x)
                else: vals[k] = x
            return len(sub) - len(vals)
        
        return sum(fn(arr[i:len(arr):k]) for i in range(k))