# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val        # Value of the node
#         self.left = left      # Pointer to the left child node
#         self.right = right    # Pointer to the right child node

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: if the current node is None (i.e., empty tree or leaf node),
        # the depth is 0 because there are no nodes to traverse.
        if not root:
            return 0
        
        # Recursively calculate the depth of the left subtree.
        l = self.maxDepth(root.left)
        
        # Recursively calculate the depth of the right subtree.
        r = self.maxDepth(root.right)
        
        # The depth of the current node is 1 (for the current node itself),
        # plus the maximum depth of either the left or right subtree.
        # We use max(l, r) to get the deepest of the two subtrees and add 1
        # for the current node.
        return max(l, r) + 1
