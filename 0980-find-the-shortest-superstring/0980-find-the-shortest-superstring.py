from typing import List
import itertools
import functools

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:

        # Function to calculate the overlap between two strings
        @functools.lru_cache(None)
        def overlap(a: str, b: str) -> int:
            max_overlap = 0
            for i in range(1, min(len(a), len(b)) + 1):
                if a[-i:] == b[:i]:
                    max_overlap = i
            return max_overlap

        # Precompute the overlap between all pairs of words
        n = len(words)
        overlaps = [[0] * n for _ in range(n)]
        for i, j in itertools.product(range(n), repeat=2):
            if i != j:
                overlaps[i][j] = overlap(words[i], words[j])

        # dp[mask][i] will be the length of the shortest superstring that contains
        # all words corresponding to the bits in mask, ending with words[i]
        dp = [[float('inf')] * n for _ in range(1 << n)]
        parent = [[None] * n for _ in range(1 << n)]
        for i in range(n):
            dp[1 << i][i] = len(words[i])

        # Iterate over all subsets of words
        for mask in range(1 << n):
            for i in range(n):
                if not (mask & (1 << i)):
                    continue
                for j in range(n):
                    if mask & (1 << j):
                        continue
                    new_mask = mask | (1 << j)
                    new_len = dp[mask][i] + len(words[j]) - overlaps[i][j]
                    if new_len < dp[new_mask][j]:
                        dp[new_mask][j] = new_len
                        parent[new_mask][j] = i

        # Reconstruct the shortest superstring
        mask = (1 << n) - 1
        min_len = float('inf')
        last = -1
        for i in range(n):
            if dp[mask][i] < min_len:
                min_len = dp[mask][i]
                last = i

        result = []
        while mask:
            result.append(words[last])
            next_last = parent[mask][last]
            mask ^= (1 << last)
            last = next_last

        result.reverse()
        superstring = result[0]
        for i in range(1, len(result)):
            overlap_len = overlap(result[i - 1], result[i])
            superstring += result[i][overlap_len:]

        return superstring