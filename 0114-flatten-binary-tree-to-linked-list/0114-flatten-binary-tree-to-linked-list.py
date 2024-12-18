# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Flattens the binary tree into a "linked list" in place, using the tree's right pointers to 
        represent the list. The order of nodes in the "linked list" follows a pre-order traversal.

        :param root: TreeNode - The root node of the binary tree.
        :return: None - The tree is modified in-place.
        """
        
        # Start with the current node as the root.
        curr = root
        while curr:
            # If the current node has a left child, we need to process it.
            if curr.left is not None:
                # Find the rightmost node in the left subtree (predecessor).
                prev = curr.left
                while prev.right:
                    prev = prev.right
                
                # Connect the right subtree of the current node to the rightmost node of the left subtree.
                prev.right = curr.right

                # Move the left subtree to the right and set the left child to None.
                curr.right = curr.left
                curr.left = None
            
            # Move to the next node in the modified tree (always moving to the right).
            curr = curr.right
