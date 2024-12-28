class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans=1
        for i,c in enumerate(word[1:]):
            if c==word[i]: ans+=1
        return ans