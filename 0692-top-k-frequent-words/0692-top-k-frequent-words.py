class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words = sorted(words)
        d = collections.Counter(words)
        sd = dict(sorted(d.items(), key = lambda kv: kv[1], reverse = True))  #It is sorting the dictionary by its value in the reverse order.
        li = []
        
        #print(sd)
        for key,v in sd.items():
            li.append(key)
        
        
        return li[:k]

        