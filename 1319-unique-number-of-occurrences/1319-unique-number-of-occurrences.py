class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        frequencies = Counter(arr).values()
        return len(set(frequencies)) == len(frequencies)