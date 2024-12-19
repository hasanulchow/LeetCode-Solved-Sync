# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize a variable to store the maximum path sum
        maxPath = -float("inf")  # A very small value as the starting point

        # Helper function to calculate the maximum gain from each subtree
        def gainFromSubtree(node: Optional[TreeNode]) -> int:
            nonlocal maxPath  # Allows modification of the outer `maxPath` variable

            # Base case: if the node is null, return 0 (no contribution)
            if not node:
                return 0

            # Recursively calculate the maximum gain from the left subtree
            # If the gain is negative, consider it as 0 (ignore it)
            gainFromLeft = max(gainFromSubtree(node.left), 0)

            # Recursively calculate the maximum gain from the right subtree
            # If the gain is negative, consider it as 0 (ignore it)
            gainFromRight = max(gainFromSubtree(node.right), 0)

            # Calculate the maximum path sum passing through this node
            # Include both left and right gains, plus the value of the current node
            maxPath = max(maxPath, gainFromLeft + gainFromRight + node.val)

            # Return the maximum gain including this node and one of its subtrees
            return max(gainFromLeft + node.val, gainFromRight + node.val)

        # Start the recursion from the root
        gainFromSubtree(root)

        # Return the maximum path sum found
        return maxPath
