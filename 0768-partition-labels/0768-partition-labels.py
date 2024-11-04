class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last ={}
        res = []
        for i in range(len(s)):
            last[s[i]] = i
        
        start = 0
        end = last[s[start]]
        i=1
        
        while(1):
            while( i < end):
                if last[s[i]]  > end:
                    end = last[s[i]]
                i += 1
            res.append(end-start+1)
            if end < len(s)-1:
                start = end+1
                end = last[s[start]]
                i = start + 1
            else:
                break
        
        return res