# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        stack, cnt = [root], 0  # Initialize stack with root and operation count
        while stack:
            new_stack = []
            for node in stack:
                # Collect nodes for the next level
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)

            # Prepare for processing the current level
            stack = new_stack
            if not stack:
                break  # No more levels to process

            # Create a mapping of node values to their current indices
            dic_level = {node.val: i for i, node in enumerate(stack)}

            # Sort the node values to determine the target order
            sort_level = sorted(dic_level.keys())

            # Use a visited set to handle cycles in swapping
            visited = set()
            for i in range(len(sort_level)):
                if sort_level[i] in visited or dic_level[sort_level[i]] == i:
                    continue

                # Perform cycle detection and counting swaps
                cycle_length, j = 0, i
                while sort_level[j] not in visited:
                    visited.add(sort_level[j])
                    j = dic_level[sort_level[j]]
                    cycle_length += 1

                # Add swaps needed for this cycle
                if cycle_length > 1:
                    cnt += cycle_length - 1

        return cnt
