# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # Result list to store the largest value in each row
        result = []

        # Queue for level-order traversal
        queue = deque([root])

        while queue:
            # Get the size of the current level
            level_size = len(queue)

            # Initialize the max value for this level
            max_value = float('-inf')

            for _ in range(level_size):
                # Pop the current node from the queue
                node = queue.popleft()

                # Update the max value for this level
                max_value = max(max_value, node.val)

                # Add the left and right children to the queue if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Append the max value of this level to the result
            result.append(max_value)

        return result