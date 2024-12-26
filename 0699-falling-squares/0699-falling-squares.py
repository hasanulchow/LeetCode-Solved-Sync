class Solution:
    def fallingSquares(self, positions):
        h = [0]*len(positions)

        for i,(l1,s1) in enumerate(positions):
            r1 = l1 + s1
            h[i] += s1
            for j in range(i+1,len(positions)):
                l2,s2 = positions[j]
                r2 = l2 + s2
                if l2 < r1 and r2 > l1:
                    h[j] = max(h[j],h[i])

        max_val, ans = 0, []

        for i in h:
            max_val = max(max_val,i)
            ans.append(max_val)

        return ans











        
        