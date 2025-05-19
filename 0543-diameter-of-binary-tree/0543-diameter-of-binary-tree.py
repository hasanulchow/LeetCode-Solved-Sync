# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def dfs(node):
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            current_diameter = left_depth + right_depth

            self.max_diameter = max(self.max_diameter, current_diameter)

            return 1 + max(left_depth, right_depth)

        dfs(root)

        return self.max_diameter
        