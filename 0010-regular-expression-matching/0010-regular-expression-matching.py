class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Cache to store results of subproblems for memoization
        cache = {}

        def dfs(i, j):
            """
            A helper function that uses depth-first search and memoization
            to determine if s[i:] matches p[j:].
            Parameters:
            - i: Current index in string `s`.
            - j: Current index in pattern `p`.
            """
            # Check if the result for this state is already cached
            if (i, j) in cache:
                return cache[(i, j)]

            # Base case: both s and p are fully matched
            if i >= len(s) and j >= len(p):
                return True

            # Base case: pattern is exhausted but s is not
            if j >= len(p):
                return False

            # Check if characters match or pattern has '.' wildcard
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            # Handle '*' wildcard in the pattern
            if (j + 1) < len(p) and p[j + 1] == '*':
                # Option 1: Skip this "char*" in the pattern (match 0 instances)
                # Option 2: Use this "char*" in the pattern if there's a match
                cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return cache[(i, j)]

            # Standard case: Characters match or '.' wildcard matches
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            # No match found
            cache[(i, j)] = False
            return False

        # Start the recursion from the beginning of both strings
        return dfs(0, 0)
