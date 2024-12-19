# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        Counts the total number of nodes in a binary tree.

        :param root: TreeNode - The root node of the binary tree.
        :return: int - The total number of nodes in the tree.
        """
        # If the tree is empty (root is None), return 0.
        if not root: 
            return 0
        
        # Recursively count nodes in the left and right subtrees,
        # then add 1 for the current node.
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
