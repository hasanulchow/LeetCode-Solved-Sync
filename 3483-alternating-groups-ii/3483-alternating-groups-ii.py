class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        for i in range(k-1):
            colors.append(colors[i])
        n = len(colors)
        res = 0
        i = 0
        j = 1
        while j<n:
            if colors[j-1]==colors[j]:
                i = j
                j+=1
                continue    
            j+=1
            if j-i<k:
                continue
            res+=1
            i+=1
        return res