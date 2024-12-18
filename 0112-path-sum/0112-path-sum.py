# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Determines if the binary tree has a root-to-leaf path such that the sum of the node values 
        along the path equals the given target sum.

        :param root: TreeNode - The root node of the binary tree.
        :param targetSum: int - The target sum to check for a root-to-leaf path.
        :return: bool - True if such a path exists, otherwise False.
        """
        
        # Base case: If the current node is None, there is no path, return False.
        if not root:
            return False

        # Check if the current node is a leaf node and its value equals the remaining targetSum.
        if not root.left and not root.right:
            return targetSum == root.val

        # Recursively check the left and right subtrees with the updated targetSum.
        # Subtract the current node's value from the targetSum for the recursive calls.
        left_sum = self.hasPathSum(root.left, targetSum - root.val)
        right_sum = self.hasPathSum(root.right, targetSum - root.val)

        # Return True if either the left or right subtree has a valid path.
        return left_sum or right_sum
