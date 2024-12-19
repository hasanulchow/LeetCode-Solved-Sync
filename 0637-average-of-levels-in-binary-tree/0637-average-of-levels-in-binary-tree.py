from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # Handle case where the tree is empty
        if not root:
            return []
        
        # Result list to store the average of each level
        result = []
        
        # Queue for level order traversal (BFS), initialized with the root node
        queue = deque([root])
        
        # Start level order traversal, processing one level at a time
        while queue:
            # The number of nodes at the current level
            level_size = len(queue)
            
            # Variable to accumulate the sum of node values at the current level
            level_sum = 0
            
            # Process all nodes at the current level
            for _ in range(level_size):
                # Pop the leftmost node from the queue
                node = queue.popleft()
                
                # Add the node value to the sum for this level
                level_sum += node.val
                
                # Add the left child to the queue if it exists
                if node.left:
                    queue.append(node.left)
                
                # Add the right child to the queue if it exists
                if node.right:
                    queue.append(node.right)
            
            # After processing the current level, calculate the average
            # and append it to the result list
            result.append(level_sum / level_size)
        
        # Return the result list containing the averages of each level
        return result
