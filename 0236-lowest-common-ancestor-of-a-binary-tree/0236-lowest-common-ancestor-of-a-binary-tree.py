# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base case: if the current node is None or matches one of p or q
        if not root:
            return None
        if root == p or root == q:
            return root
        
        # Recursively search for LCA in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right are not None, the current root is the LCA
        if left and right:
            return root
        
        # If one of left or right is None, return the non-null result (either left or right)
        return left if left else right
