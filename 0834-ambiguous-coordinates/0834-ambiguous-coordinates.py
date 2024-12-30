class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s.strip("(").strip(")")
        
        def fn(s): 
            """Return valid numbers from s."""
            if len(s) == 1: return [s]
            if s.startswith("0") and s.endswith("0"): return []
            if s.startswith("0"): return [s[:1] + "." + s[1:]]
            if s.endswith("0"): return [s]
            return [s[:i] + "." + s[i:] for i in range(1, len(s))] + [s]
        
        ans = []
        for i in range(1, len(s)): 
            for x in fn(s[:i]):
                for y in fn(s[i:]): 
                    ans.append(f"({x}, {y})")
        return ans  