from queue import Queue
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, A: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty, return an empty list
        if not A:
            return []
        
        # Initialize a queue for level-order traversal
        queue = Queue()
        queue.put(A)
        
        # List to store the final zigzag order traversal result
        output = []
        
        # Temporary list to store nodes at the current level
        curr = []
        
        # Variable to track whether the current level is even or odd
        level = 0
        
        # Perform level-order traversal using the queue
        while not queue.empty():
            # Get the number of nodes at the current level
            size = queue.qsize()
            
            # Reset the current level list
            curr = []
            
            # Process each node at the current level
            for i in range(size):
                # Get the node from the queue
                temp = queue.get()
                
                # If the current level is even, append the node value normally
                # If the current level is odd, insert the node value at the beginning
                if level % 2 == 0:
                    curr.append(temp.val)
                else:
                    curr.insert(0, temp.val)
                
                # Add left and right children of the current node to the queue
                if temp.left:
                    queue.put(temp.left)
                if temp.right:
                    queue.put(temp.right)
            
            # Toggle the level to switch between even and odd
            level = not level
            
            # Add the current level's values to the output list
            output.append(curr)
        
        # Return the zigzag order traversal result
        return output
