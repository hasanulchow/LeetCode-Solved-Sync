class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_counts = Counter()
        
        for word in words2:
            counts = Counter(word)
            max_counts |= counts
        
        universal_strings = []
        
        for word in words1:
            counts = Counter(word)
            if all(counts[char] >= max_counts[char] for char in max_counts):
                universal_strings.append(word)
        
        return universal_strings