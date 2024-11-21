from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Initialize the grid, with 0 meaning unguarded.
        g = [[0] * n for _ in range(m)]

        # Place the guards (represented by 1) on the grid.
        for r, c in guards:
            g[r][c] = 1
        
        # Place the walls (represented by 2) on the grid.
        for r, c in walls:
            g[r][c] = 2

        def mark_guarded(r, c):
            # Mark all cells that a guard can watch in four directions: down, up, right, left.
            
            # Mark down direction
            for row in range(r + 1, m):
                if g[row][c] in [1, 2]:  # Stop if there's another guard or wall
                    break
                g[row][c] = 3  # Mark as guarded
            
            # Mark up direction
            for row in reversed(range(0, r)):
                if g[row][c] in [1, 2]:
                    break
                g[row][c] = 3
            
            # Mark right direction
            for col in range(c + 1, n):
                if g[r][col] in [1, 2]:
                    break
                g[r][col] = 3
            
            # Mark left direction
            for col in reversed(range(0, c)):
                if g[r][col] in [1, 2]:
                    break
                g[r][col] = 3

        # Mark all cells guarded by each guard
        for r, c in guards:
            mark_guarded(r, c)

        # Count all unguarded cells (cells with value 0)
        res = 0
        for row in g:
            for cell in row:
                if cell == 0:  # Unguarded cells are marked as 0
                    res += 1

        return res
