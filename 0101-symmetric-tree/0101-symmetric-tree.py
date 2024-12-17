# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if a binary tree is symmetric around its center.
        
        :param root: The root of the binary tree.
        :return: True if the tree is symmetric, otherwise False.
        """
        
        # Helper function to check if two subtrees are mirrors of each other
        def is_mirror(n1, n2):
            """
            Recursively checks if two nodes and their subtrees are mirror images.
            
            :param n1: First tree node.
            :param n2: Second tree node.
            :return: True if the subtrees are mirrors, otherwise False.
            """
            # If both nodes are None, they are mirrors
            if not n1 and not n2:
                return True
            
            # If only one of the nodes is None, they are not mirrors
            if not n1 or not n2:
                return False
            
            # Check if the values of the nodes are equal and 
            # their children are mirrors (left with right, right with left)
            return n1.val == n2.val and is_mirror(n1.left, n2.right) and is_mirror(n1.right, n2.left)
        
        # A tree is symmetric if the left and right subtrees are mirrors
        return is_mirror(root.left, root.right)
