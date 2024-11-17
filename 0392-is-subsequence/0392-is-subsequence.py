class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l=[[0 for i in range(len(t)+1) ] for j in range(len(s)+1)]
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i]==t[j]:
                    l[i+1][j+1]=l[i][j]+1
                else:
                    l[i+1][j+1]=max(l[i][j+1],l[i+1][j])
        if len(s)==l[len(s)][len(t)]:
            return True
        else:
            return False