# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns the values of the nodes visible from the right side of the binary tree.

        Args:
        root (TreeNode): The root of the binary tree.

        Returns:
        List[int]: A list of integers representing the values visible from the right side.
        """
        ans = []  # To store the right-side view of the tree
        if root is None:  # If the tree is empty, return an empty list
            return ans

        # Use a deque for level-order traversal (BFS)
        temp = deque([root])  # Start with the root node
        while temp:
            l = len(temp)  # Number of nodes in the current level
            val = 0  # Placeholder for the rightmost node value in the current level

            # Iterate through all nodes in the current level
            for _ in range(l):
                node = temp.popleft()  # Get the front node of the deque
                val = node.val  # Update the rightmost value (overwritten until last node)

                # Add the left child to the deque if it exists
                if node.left:
                    temp.append(node.left)
                # Add the right child to the deque if it exists
                if node.right:
                    temp.append(node.right)

            # Add the rightmost node's value to the result
            ans.append(val)

        return ans
