from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty, return an empty list
        if not root:
            return []
        
        # List to store the result of level order traversal
        ans = []
        
        # Initialize a queue with the root node to begin the traversal
        queue = [root]
        
        # Perform level order traversal (Breadth-First Search)
        while queue:
            # Get the number of nodes at the current level
            level_size = len(queue)
            
            # List to store node values at the current level
            level = []
            
            # Process all nodes at the current level
            for i in range(level_size):
                # Pop the leftmost node from the queue
                node = queue.pop(0)
                
                # Add the node's value to the current level list
                level.append(node.val)
                
                # If the left child exists, add it to the queue
                if node.left:
                    queue.append(node.left)
                
                # If the right child exists, add it to the queue
                if node.right:
                    queue.append(node.right)
            
            # After processing all nodes at the current level, add the level to the result
            ans.append(level)
        
        # Return the result list, which contains lists of node values for each level
        return ans
