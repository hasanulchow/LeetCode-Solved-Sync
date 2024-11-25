from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Flatten the board into a tuple (state)
        state = tuple(board[0] + board[1])
        
        # Define the possible moves from each position of the 0 (empty space)
        moves = {
            0: [1, 3],  # Empty space at index 0 can move to index 1 or 3
            1: [0, 2, 4],  # Empty space at index 1 can move to index 0, 2, or 4
            2: [1, 5],  # Empty space at index 2 can move to index 1 or 5
            3: [0, 4],  # Empty space at index 3 can move to index 0 or 4
            4: [1, 3, 5],  # Empty space at index 4 can move to index 1, 3, or 5
            5: [2, 4],  # Empty space at index 5 can move to index 2 or 4
        }
        
        # The goal state we are trying to reach
        target = (1, 2, 3, 4, 5, 0)
        
        # Initialize BFS queue, seen set, and move count
        queue, seen, cnt = deque([state]), set([state]), 0
        
        while queue:
            for _ in range(len(queue)):
                state = queue.popleft()
                
                # Check if we've reached the target state
                if state == target:
                    return cnt
                
                # Find the index of the empty space (0)
                idx = state.index(0)
                
                # Try all valid moves for the empty space
                for i in moves[idx]:
                    # Create a new state by swapping the empty space (0) with another tile
                    curr = list(state)
                    curr[idx], curr[i] = curr[i], curr[idx]
                    new_state = tuple(curr)
                    
                    # If the new state has not been seen, add it to the queue and mark as seen
                    if new_state not in seen:
                        queue.append(new_state)
                        seen.add(new_state)
            
            # Increment the move count after processing all nodes at the current depth
            cnt += 1
        
        return -1  # If no solution is found
