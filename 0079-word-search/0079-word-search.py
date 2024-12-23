class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
    
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, k):
            # Base case: if we've matched the entire word
            if k == len(word):
                return True

            # If out of bounds, already visited, or current cell doesn't match the word's character
            if not (0 <= r < rows) or not (0 <= c < cols) or (r, c) in visited or board[r][c] != word[k]:
                return False

            # Mark the cell as visited
            visited.add((r, c))

            # Explore all 4 directions (up, down, left, right)
            res = dfs(r + 1, c, k + 1) or dfs(r - 1, c, k + 1) or dfs(r, c + 1, k + 1) or dfs(r, c - 1, k + 1)

            # Backtrack by removing the current cell from the visited set
            visited.remove((r, c))
            
            return res

        # Count the frequency of characters in the word
        count = {}
        for c in word:
            count[c] = 1 + count.get(c, 0)

        # Reverse the word if the first character appears less often than the last
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        # Try starting the search from each cell in the board
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False
