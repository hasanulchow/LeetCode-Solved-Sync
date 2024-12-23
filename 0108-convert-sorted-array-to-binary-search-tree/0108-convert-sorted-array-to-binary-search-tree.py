# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Base case: If the input list is empty, return None
        if not nums:
            return None

        # Find the middle element to use as the root
        mid = len(nums) // 2

        # Create a TreeNode with the middle element
        root = TreeNode(nums[mid])

        # Recursively build the left subtree with the left half of the list
        root.left = self.sortedArrayToBST(nums[:mid])

        # Recursively build the right subtree with the right half of the list
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        # Return the constructed tree's root
        return root
