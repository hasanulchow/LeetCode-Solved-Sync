class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # Define a DFS function to traverse the board and search for words
        def dfs(x, y, root):
            """
            A helper function to perform depth-first search on the board to find words.
            Parameters:
            - x, y: Current position on the board.
            - root: Current node in the trie.
            """
            letter = board[x][y]  # Get the letter at the current position on the board
            cur = root[letter]  # Traverse the trie to the next node using the letter
            word = cur.pop('#', False)  # Check if the node contains a word (denoted by '#')
            
            if word:
                # If a word is found, add it to the results list
                res.append(word)
            
            board[x][y] = '*'  # Mark the current position on the board as visited
            
            # Recursively search in all four directions (right, left, down, up)
            for dirx, diry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                curx, cury = x + dirx, y + diry
                # Check if the next position is within the board's bounds and the next letter exists in the trie
                if 0 <= curx < m and 0 <= cury < n and board[curx][cury] in cur:
                    dfs(curx, cury, cur)  # Continue DFS search from the new position
            
            board[x][y] = letter  # Restore the original value of the current position on the board
            
            # If the current node has no children, remove it from the trie to prune unused nodes
            if not cur:
                root.pop(letter)
        
        # Step 1: Build a trie data structure from the list of words
        trie = {}
        for word in words:
            cur = trie
            for letter in word:
                cur = cur.setdefault(letter, {})  # Add the letter to the trie, create a new node if needed
            cur['#'] = word  # Mark the end of a word in the trie by using the '#' symbol
            
        # Step 2: Get the dimensions of the board (number of rows and columns)
        m, n = len(board), len(board[0])
        
        # Step 3: Initialize a list to store the results
        res = []
        
        # Step 4: Traverse the board and start DFS from each cell that has a letter in the trie
        for i in range(m):
            for j in range(n):
                # If the current letter is in the trie, begin the DFS search
                if board[i][j] in trie:
                    dfs(i, j, trie)
        
        # Step 5: Return the list of found words
        return res
