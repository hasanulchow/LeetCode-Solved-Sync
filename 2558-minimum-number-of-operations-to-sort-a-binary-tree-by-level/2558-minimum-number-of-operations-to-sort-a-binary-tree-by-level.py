# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        # Initialize the queue for level order traversal and the operation count
        queue = deque([root])
        operations = 0

        while queue:
            # For each level, collect the values of nodes
            level_values = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Map each value to its current index for this level
            index_map = {val: i for i, val in enumerate(level_values)}

            # Sort the level values to know the target order
            sorted_values = sorted(level_values)

            # Minimum swaps needed to sort the level
            visited = [False] * len(level_values)
            for i in range(len(level_values)):
                if visited[i] or index_map[sorted_values[i]] == i:
                    continue

                # Cycle detection for swapping
                cycle_length, j = 0, i
                while not visited[j]:
                    visited[j] = True
                    j = index_map[sorted_values[j]]
                    cycle_length += 1

                # Add the number of swaps for this cycle (cycle_length - 1)
                operations += cycle_length - 1

        return operations
