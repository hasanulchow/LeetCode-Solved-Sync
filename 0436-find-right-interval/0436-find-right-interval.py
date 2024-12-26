class Solution:
    def findRightInterval(self, intervals):
        ints = sorted([[j,k,i] for i,[j,k] in enumerate(intervals)])
        begs = [i for i,_,_ in ints]
        out = [-1]*len(begs)
        for i,j,k in ints:
            t = bisect.bisect_left(begs, j)
            if t < len(begs):
                out[k] = ints[t][2]
        
        return out