# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # Returns maximum value from the pair: [includeRoot, excludeRoot]
        result = self.heist(root)
        return max(result[0], result[1])

    def heist(self, root: Optional[TreeNode]) -> List[int]:
        # Empty tree case
        if root is None:
            return [0, 0]

        # Recursively calculating the maximum amount that can be robbed
        # from the left subtree of the root
        leftSubtree = self.heist(root.left)

        # Recursively calculating the maximum amount that can be 
        # robbed from the right subtree of the root
        rightSubtree = self.heist(root.right)

        # includeRoot contains the maximum amount of money that can be
        # robbed with the parent node included
        includeRoot = root.val + leftSubtree[1] + rightSubtree[1]

        # excludeRoot contains the maximum amount of money that can be
        # robbed with the parent node excluded
        excludeRoot = max(leftSubtree[0], leftSubtree[1]) + max(
            rightSubtree[0], rightSubtree[1]
        )

        return [includeRoot, excludeRoot]