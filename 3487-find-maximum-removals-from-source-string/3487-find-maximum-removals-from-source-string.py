class Solution:
    def maxRemovals(self, source: str, pattern: str, removableIndices: List[int]) -> int:
        source_len, pattern_len = len(source), len(pattern)
        dp = [math.inf] * (pattern_len + 1)
        dp[0] = 0  # Zero cost to match an empty pattern
        removable_set = set(removableIndices)
        
        for i in range(1, source_len + 1):
            for j in range(min(i, pattern_len), 0, -1):
                # By default, skip source[i - 1]
                if source[i - 1] == pattern[j - 1]:
                    # Try to match source[i - 1] with pattern[j - 1]
                    cost = dp[j - 1]
                    if (i - 1) in removable_set:
                        cost += 1  # Need to keep this index, increase cost
                    dp[j] = min(dp[j], cost)
        if dp[pattern_len] == math.inf:
            return 0  # Pattern cannot be matched
        max_removable = len(removableIndices) - dp[pattern_len]
        return max_removable