class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        l={arr.count(i):i for i in arr}
        return len(l) == len(set(arr))