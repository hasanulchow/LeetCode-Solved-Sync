class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        arr = [0] * n  # Array to mark valid parentheses positions
        stack = []     # Stack to track indices of unmatched '('

        # First pass: Mark valid parentheses
        for i in range(n):
            if s[i] == '(':
                stack.append(i)  # Store index of '('
            elif s[i] == ')' and stack:
                arr[stack.pop()] = 1  # Match a '(' with this ')'
                arr[i] = 1            # Mark as valid

        # Second pass: Find the longest contiguous segment of 1's in `arr`
        ans = 0  # Maximum length of valid parentheses
        temp = 0 # Current length of contiguous valid parentheses
        for i in arr:
            if i == 1:  # If valid parentheses
                temp += 1
                ans = max(ans, temp)  # Update maximum length
            else:
                temp = 0  # Reset current length if invalid

        return ans
