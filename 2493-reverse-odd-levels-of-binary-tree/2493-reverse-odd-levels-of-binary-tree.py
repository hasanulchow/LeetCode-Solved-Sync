from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Reverse the values of nodes at odd levels in a binary tree.
        :param root: TreeNode - The root of the binary tree.
        :return: TreeNode - The root of the modified binary tree.
        """
        # Initialize a queue for level-order traversal
        q = deque()
        q.append(root)
        
        # Boolean flag to track whether the current level is odd
        rev = False
        
        # Perform level-order traversal
        while q:
            # Get the number of nodes at the current level
            qz = len(q)
            arr = []  # Temporary list to store nodes at the current level
            
            # Iterate through the nodes of the current level
            for i in range(qz):
                Node = q.popleft()  # Get the next node from the queue
                
                # Add the children of the current node to the queue for the next level
                if Node.left:
                    q.append(Node.left)
                if Node.right:
                    q.append(Node.right)
                
                # If the current level is odd, add nodes to the array for reversal
                if rev:
                    arr.append(Node)
                    # Reverse the values symmetrically for nodes at odd levels
                    if i >= qz / 2:
                        arr[i].val, arr[qz - 1 - i].val = arr[qz - 1 - i].val, arr[i].val
            
            # Toggle the `rev` flag for the next level
            rev = not rev
        
        # Return the modified tree
        return root
