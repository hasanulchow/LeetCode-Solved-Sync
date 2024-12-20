from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        Find the minimum absolute difference between values of any two nodes in a BST.
        :param root: TreeNode - The root of the binary tree.
        :return: int - The minimum absolute difference between values of any two nodes.
        """
        # Initialize a deque for level-order traversal
        dq = deque()
        dq.append(root)

        # List to store all node values
        array = []
        
        # Perform level-order traversal to collect all node values
        while dq:
            # Get the next node from the deque
            value = dq.popleft()
            array.append(value.val)

            # Add left and right children to the deque if they exist
            if value.left:
                dq.append(value.left)
            if value.right:
                dq.append(value.right)

        # Sort the array of node values to prepare for finding minimum differences
        array.sort()

        # Initialize the minimum difference as infinity
        answer = float("inf")
        
        # Iterate through the sorted values to find the smallest difference
        for i in range(1, len(array)):
            # Calculate the difference between consecutive elements
            answer = min(answer, array[i] - array[i - 1])

            # Early exit if the minimum possible difference (1) is found
            if answer == 1:
                break

        return answer
