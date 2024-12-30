class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def groupWord(word):
            size = 1
            for i in range(1, len(word)):
                if word[i] == word[i - 1]:
                    size += 1
                else:
                    yield word[i - 1], size
                    size = 1
            
            yield word[-1], size
            yield ' ', 0
        
        res = len(words)
        
        for word in words:
            for (sChar, sSize), (wordChar, wordSize) in zip(groupWord(s), groupWord(word)):
                if sChar != wordChar or sSize < wordSize or wordSize < sSize < 3:
                    res -= 1
                    break
        
        return res