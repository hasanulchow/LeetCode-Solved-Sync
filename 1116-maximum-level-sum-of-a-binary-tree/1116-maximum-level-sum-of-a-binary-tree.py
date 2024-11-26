# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        levels = defaultdict(int)
        def recSolve(root: Optional[TreeNode], level: int = 0) -> None:
            nonlocal levels

            if not root:
                return 

            levels[level] += root.val

            recSolve(root.left, level+1)
            recSolve(root.right, level+1)

        recSolve(root)

        sums = [v for (i, v) in levels.items()]
        return sums.index(max(sums)) + 1
        