from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Perform a zigzag level order traversal of a binary tree.
        :param root: TreeNode - The root node of the binary tree.
        :return: List[List[int]] - The zigzag level order traversal as a list of lists.
        """
        # If the tree is empty, return an empty list
        if root is None:
            return []

        # Initialize a deque for level-order traversal
        queue = deque()
        queue.append(root)  # Start with the root node
        
        # List to store the zigzag level order traversal
        ans = []

        # Boolean to toggle zigzag order
        zigzag = False

        # Perform level-order traversal
        while queue:
            level = []  # List to store nodes at the current level
            n = len(queue)  # Number of nodes at the current level

            for i in range(n):
                # Pop a node from the deque
                node = queue.popleft()
                level.append(node.val)  # Add its value to the current level list

                # Add left and right children to the deque if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Reverse the level list if zigzag is True
            if zigzag:
                level.reverse()
            
            # Append the current level to the result
            ans.append(level)

            # Toggle the zigzag flag for the next level
            zigzag = not zigzag

        return ans
