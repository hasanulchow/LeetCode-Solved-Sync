from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Perform a level-order traversal (breadth-first search) on a binary tree.
        :param root: TreeNode - The root of the binary tree.
        :return: List[List[int]] - A list of lists where each sublist contains values of nodes at a specific level.
        """
        # If the tree is empty, return an empty list
        if not root:
            return []

        # Initialize the result list and a queue for traversal
        ans = []  # Stores the final level-order traversal
        queue = [root]  # Initialize the queue with the root node
        
        # Process each level of the tree
        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            level = []  # List to store node values for the current level
            
            # Process all nodes in the current level
            for i in range(level_size):
                # Remove the first node from the queue
                node = queue.pop(0)
                # Add its value to the current level list
                level.append(node.val)
                
                # Add the left child to the queue if it exists
                if node.left:
                    queue.append(node.left)
                # Add the right child to the queue if it exists
                if node.right:
                    queue.append(node.right)
            
            # Append the current level's values to the result list
            ans.append(level)
        
        return ans
