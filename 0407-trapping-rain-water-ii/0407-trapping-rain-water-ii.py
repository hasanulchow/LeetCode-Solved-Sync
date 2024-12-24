import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        pq = []  # Priority queue (min-heap) to process the cells in increasing height order
        seen = set()  # Set to keep track of visited cells
        
        grid = heightMap  # The given heightMap grid
        self._enqueue_boundaries(grid, pq, seen)  # Enqueue all the boundary cells
        
        max_height = -float("inf")  # Variable to keep track of the highest height encountered so far
        ans = 0  # Variable to accumulate the total amount of trapped water
        
        # Process cells from the boundary inward
        while pq:
            height, i, j = heapq.heappop(pq)  # Pop the cell with the smallest height
            if height < max_height:
                # If the current height is lower than the max_height encountered so far,
                # it means water can be trapped between the current cell and max_height
                ans += max_height - height  # Calculate the trapped water and add to answer
            else:
                # Otherwise, update the max_height to the current cell's height
                max_height = height
            
            # Get all the neighboring cells (right, down, left, up)
            neighbors = [(i, j+1), (i+1, j), (i-1, j), (i, j-1)]
            # Enqueue all the unvisited neighbors into the priority queue
            for x, y in neighbors:
                self._enqueue_elem(grid, x, y, pq, seen)
                
        return ans  # Return the total trapped water
    
    def _enqueue_boundaries(self, grid, pq, seen):
        # Enqueue all the boundary cells (top, bottom, left, right edges)
        self._enqueue_top_bottom(grid, pq, seen)
        self._enqueue_left_right(grid, pq, seen)
        
    def _enqueue_top_bottom(self, grid, pq, seen):
        # Enqueue the top and bottom rows
        bottom_row_indx = len(grid)-1
        
        for i in range(len(grid[0])):
            self._enqueue_elem(grid, 0, i, pq, seen)  # Top row cell (0, i)
            self._enqueue_elem(grid, bottom_row_indx, i, pq, seen)  # Bottom row cell (bottom_row_indx, i)
    
    def _enqueue_left_right(self, grid, pq, seen):
        # Enqueue the left and right columns
        last_col_indx = len(grid[0]) - 1
        
        for i in range(len(grid)):
            self._enqueue_elem(grid, i, 0, pq, seen)  # Left column cell (i, 0)
            self._enqueue_elem(grid, i, last_col_indx, pq, seen)  # Right column cell (i, last_col_indx)
            
    def _enqueue_elem(self, grid, i, j, pq, seen):
        # Check if the current position (i, j) is within bounds and not yet visited
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i, j) not in seen:
            heapq.heappush(pq, (grid[i][j], i, j))  # Push the current cell into the min-heap with its height
            seen.add((i, j))  # Mark this cell as visited
