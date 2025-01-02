# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # Helper function for DFS traversal
        def dfs(node, current_depth):
            if not node:
                return
            if current_depth == depth - 1:  # We reached the depth before the insertion point
                # Insert new nodes
                node.left = TreeNode(val=val, left=node.left)
                node.right = TreeNode(val=val, right=node.right)
                return
            # Continue DFS traversal
            dfs(node.left, current_depth + 1)
            dfs(node.right, current_depth + 1)

        if depth == 1:  # Special case for depth 1
            new_root = TreeNode(val=val, left=root)
            return new_root
        else:
            dfs(root, 1)
            return root