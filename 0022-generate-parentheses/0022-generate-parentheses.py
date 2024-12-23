class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openP, closeP, s):
            # If the number of open and close parentheses is equal to n,
            # and the total length is 2*n, we found a valid combination.
            if openP == closeP and openP + closeP == n * 2:
                res.append(s)
                return
            
            # If we still have open parentheses to add, we can add "("
            if openP < n:
                dfs(openP + 1, closeP, s + "(")
            
            # If we have more open parentheses than close parentheses,
            # we can add ")"
            if closeP < openP:
                dfs(openP, closeP + 1, s + ")")

        # Start the recursion with 0 open and close parentheses
        dfs(0, 0, "")

        return res
