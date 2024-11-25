class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # Variable to keep track of the longest zigzag path
        maxLen = 0

        # Helper function for DFS traversal
        def dfs(node, dir, len):
            # If the node is None, stop the recursion
            if not node:
                return

            nonlocal maxLen
            # Update the maximum zigzag length found so far
            maxLen = max(maxLen, len)

            # Explore the left child (if coming from right)
            # If direction was "right", continue the zigzag by moving left with length increased
            # Otherwise, reset the length to 1 (new zigzag path)
            dfs(node.left, "left", len + 1 if dir == "right" else 1)

            # Explore the right child (if coming from left)
            # If direction was "left", continue the zigzag by moving right with length increased
            # Otherwise, reset the length to 1 (new zigzag path)
            dfs(node.right, "right", len + 1 if dir == "left" else 1)

        # If the tree is empty, return 0 (no zigzag path)
        if not root:
            return maxLen

        # Start DFS with both directions from the root node
        # We start with the left child of root, assuming we first move left, with a path length of 1
        dfs(root.left, "left", 1)
        # We start with the right child of root, assuming we first move right, with a path length of 1
        dfs(root.right, "right", 1)

        # Return the maximum zigzag length found
        return maxLen
