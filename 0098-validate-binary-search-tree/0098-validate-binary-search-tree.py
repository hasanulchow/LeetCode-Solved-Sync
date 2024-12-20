# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper function to check the validity of the BST.
        def valid(node, minimum, maximum):
            # Base case: if the node is None, it's a valid subtree (empty tree is always valid).
            if not node:
                return True
            
            # If the node's value is not within the valid range, return False.
            if not (node.val > minimum and node.val < maximum):
                return False
            
            # Recursively check the left and right subtrees:
            # Left subtree should have all values less than the current node value.
            # Right subtree should have all values greater than the current node value.
            return valid(node.left, minimum, node.val) and valid(node.right, node.val, maximum)
        
        # Initialize the recursion with the entire range of valid values (-inf to +inf).
        return valid(root, float("-inf"), float("inf"))
