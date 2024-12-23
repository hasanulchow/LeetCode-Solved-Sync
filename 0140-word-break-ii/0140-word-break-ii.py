from collections import defaultdict

def fun(s, dc, memo):
    # If the result for the string `s` is already computed, return it from memoization
    if s in memo:
        return memo[s]
    
    ans = []
    
    # If the current string `s` is a valid word, add it as a valid answer
    if dc[s] == 1:
        ans = [s]
    
    # Try splitting the string and solving recursively for the right part
    for i in range(1, len(s)):
        if dc[s[:i]] == 1:  # If the prefix `s[:i]` is a valid word
            # Recursively solve for the remaining part `s[i:]`
            a = fun(s[i:], dc, memo)
            for x in a:
                ans.append(s[:i] + " " + x)  # Combine prefix with valid suffixes
    
    # Store the result in memo before returning
    memo[s] = ans
    return ans

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Create a dictionary to store words for O(1) lookup
        dc = defaultdict(lambda: 0)
        
        # Mark valid words in the dictionary
        for word in wordDict:
            dc[word] = 1
        
        # Call the helper function `fun` to get all possible valid word breaks
        return fun(s, dc, {})
