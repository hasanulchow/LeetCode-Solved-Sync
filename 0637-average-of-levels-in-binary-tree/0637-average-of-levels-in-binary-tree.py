# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> list:
        """
        Calculate the average value of the nodes on each level of the binary tree.
        :param root: TreeNode - The root of the binary tree.
        :return: list[float] - A list of averages for each level.
        """
        # Handle the case where the tree is empty
        if not root:
            return []
        
        # Initialize result list to store averages and a queue for level-order traversal
        result = []  # List to store average values of each level
        queue = [root]  # Queue to keep track of nodes at each level
        
        # Traverse the tree level by level
        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            level_sum = 0  # Sum of all node values at the current level
            next_queue = []  # Temporary list for the next level's nodes
            
            # Process all nodes in the current level
            for node in queue:
                # Add the node's value to the level sum
                level_sum += node.val
                
                # Add the node's children to the next level's queue
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            
            # Calculate and store the average for the current level
            result.append(level_sum / level_size)
            # Move to the next level
            queue = next_queue
        
        return result
