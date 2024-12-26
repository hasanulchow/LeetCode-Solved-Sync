class Solution:
    def __init__(self):
        self.cache = {}

    def f(self, s, i, j):
        if i > j:
            return 0
        if i == j: 
            return 1
        if (i, j) in self.cache: 
            return self.cache[(i, j)]

        if s[i] == s[j]:
            low, high = i + 1, j - 1
            while low <= high and s[low] != s[i]: 
                low += 1
            while low <= high and s[high] != s[j]: 
                high -= 1

            if low > high:  
                # f(abcba) => f(bcb), a+f(bcb)+a, a, aa
                res = self.f(s, i+1, j-1) * 2 + 2 
            elif low == high:  
                # exactly one matching a inside, eg f(ababa) => f(bcb), a + f(bcb) + a, aa (a already included)
                res = self.f(s, i+1, j-1) * 2 + 1
            else:  
                # eg. f(aabcbaa) => {a + f(abcba) + a, f(abcba)} - {f(bcb)}
                # why subtract?
                # when we add the outer 'a's to form palindromes, the palindromes that start and end with 'a' (like "aa", "aba") within "abcba" 
                # are effectively counted a second time as unique palindromes, hence correct overcounting
                res = self.f(s, i+1, j-1) * 2 - self.f(s, low+1, high-1)
        else:
            # eg. f(abcbx) => f(abcb) + f(bcbx) - f(bcb)
            res = self.f(s, i, j-1) + self.f(s, i+1, j) - self.f(s, i+1, j-1)

        self.cache[(i, j)] = res % 1000000007
        return self.cache[(i, j)]
    
    def countPalindromicSubsequences(self, s: str) -> int:
        return self.f(s, 0, len(s) - 1)
    