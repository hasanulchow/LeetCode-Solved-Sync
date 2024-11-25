# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(root, count, maxval):
            if root.val >= maxval:
                count += 1
            if root.left:
                count = traverse(root.left, count, max(root.val, maxval))
            if root.right:
                count = traverse(root.right, count, max(root.val, maxval))
            return count

        return traverse(root, 0, root.val)
        