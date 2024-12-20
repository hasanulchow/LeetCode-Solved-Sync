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
        """
        Calculate the average value of the nodes on each level of the binary tree.
        :param root: TreeNode - The root of the binary tree.
        :return: List[float] - A list of averages for each level.
        """
        # Handle the case where the tree is empty
        if not root:
            return []
        
        # Initialize result list to store averages and a queue for level-order traversal
        result = []  # List to store average values of each level
        queue = deque([root])  # Queue to keep track of nodes at each level
        
        # Traverse the tree level by level
        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            level_sum = 0  # Sum of all node values at the current level
            
            # Process all nodes in the current level
            for _ in range(level_size):
                # Remove a node from the front of the queue
                node = queue.popleft()
                # Add its value to the level sum
                level_sum += node.val
                
                # Add the node's children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Calculate and store the average for the current level
            result.append(level_sum / level_size)
        
        return result
