# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)

    def dfs(self, node: Optional[TreeNode], num: int) -> int:
        if not node:
            return 0

        # Compute the current number by appending the node's value
        current_num = num * 10 + node.val

        # If the current node is a leaf, return the current number
        if not node.left and not node.right:
            return current_num

        # Sum the results of the left and right subtrees
        return self.dfs(node.left, current_num) + self.dfs(node.right, current_num)
