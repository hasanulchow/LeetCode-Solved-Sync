# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxLen = 0

        def dfs(node, dir, len):
            if not node: return

            nonlocal maxLen
            maxLen = max(maxLen, len)
            dfs(node.left, "left", len+1 if dir == "right" else 1)
            dfs(node.right, "right", len+1 if dir == "left" else 1)

        if not root: return maxLen
        dfs(root.left, "left", 1)
        dfs(root.right, "right", 1)
        return maxLen


        