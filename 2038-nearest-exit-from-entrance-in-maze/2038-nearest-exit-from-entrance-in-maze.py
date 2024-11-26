from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Directions for BFS (right, left, down, up)
        entrance = (entrance[0], entrance[1])  # Tuple for entrance
        q = deque([entrance])
        visited = set()
        visited.add(entrance)
        step = 0
        
        # Perform BFS
        while q:
            stepLength = len(q)

            for i in range(stepLength):
                node = q.popleft()
                
                # Check if node is at the boundary and is an exit
                if (node[0] == 0 or node[0] == len(maze) - 1 or node[1] == 0 or node[1] == len(maze[0]) - 1):
                    if maze[node[0]][node[1]] == '.' and node != entrance:
                        return step  # Found the nearest exit

                # Explore the 4 possible directions
                for d in dirs:
                    newD = (node[0] + d[0], node[1] + d[1])
                    
                    # Check if newD is within bounds, unvisited, and walkable
                    if (0 <= newD[0] < len(maze) and 0 <= newD[1] < len(maze[0]) 
                        and maze[newD[0]][newD[1]] == '.' and newD not in visited):
                        visited.add(newD)
                        q.append(newD)

            step += 1

        return -1  # No exit found
