"""
Runtime: 52 ms, faster than 95.31% of Python3 online submissions for N-Queens.
Memory Usage: 14.3 MB, less than 26.71% of Python3 online submissions for N-Queens.

Goal: Place queens such that no two queens attack each other.
Approach: Backtracking
- Each recursive layer decides on a row and the placement of the queen.
- The constraints ensure that queens are not placed in positions where they can attack each other:
    1) Make sure it is not in the same column --> use a column set.
    2) Make sure it is not in the same diagonal path --> use a diagonal set (calculated via r+c).
    3) Make sure it is not in the same anti-diagonal path --> use an antidiagonal set (calculated via r-c).
    
    Note: We do not need to worry about rows because the backtracking parameter always recurses
    to the next row level.
    
    ** Note: If you do not understand why r+c and r-c represent diagonal paths, draw it out on a grid
    and observe the pattern!
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []
        
        # Sets to track constraints
        col = set()         # Columns where queens are placed
        diagonal = set()    # Diagonal constraints (r + c)
        antidiagonal = set()# Antidiagonal constraints (r - c)
        output = []         # Temporary storage for board configuration
        result = []         # Final list of all valid solutions
        
        def backtrack(r):
            """Helper function to perform backtracking."""
            nonlocal n, col, diagonal, antidiagonal, output, result
            
            # Base case: If all rows are processed, store the valid configuration
            if r == n:
                result.append(output[:])  # Append a deep copy of the current board
                return
            
            # Iterate through each column in the current row
            for c in range(n):
                # Skip positions that violate constraints
                if c in col or (r + c) in diagonal or (r - c) in antidiagonal:
                    continue
                
                # Place the queen and update constraints
                col.add(c)
                diagonal.add(r + c)
                antidiagonal.add(r - c)
                output.append('.' * c + 'Q' + '.' * (n - c - 1))  # Construct row with queen
                
                # Recurse to the next row
                backtrack(r + 1)
                
                # Remove the queen and backtrack
                col.remove(c)
                diagonal.remove(r + c)
                antidiagonal.remove(r - c)
                output.pop()
        
        # Start backtracking from the first row
        backtrack(0)
        return result
