# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        Perform a zigzag level order traversal of a binary tree.
        :param root: TreeNode - The root node of the binary tree.
        :return: List[List[int]] - The zigzag level order traversal as a list of lists.
        """
        # If the tree is empty, return an empty list
        if root is None:
            return []

        # Use a list to simulate a queue for level-order traversal
        queue = [root]  # Start with the root node
        
        # List to store the zigzag level order traversal
        ans = []

        # Boolean to toggle zigzag order
        zigzag = False

        # Perform level-order traversal
        while queue:
            level = []  # List to store nodes at the current level
            next_level = []  # Queue for the next level

            for node in queue:
                level.append(node.val)  # Add the current node's value

                # Add children to the next level's queue
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            # Reverse the level list if zigzag is True
            if zigzag:
                level.reverse()
            
            # Append the current level to the result
            ans.append(level)

            # Update the queue with nodes of the next level
            queue = next_level

            # Toggle the zigzag flag for the next level
            zigzag = not zigzag

        return ans
