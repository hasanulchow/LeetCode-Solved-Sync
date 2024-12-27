class Solution:
    def dfs(self, node1: TreeNode, node2: TreeNode) -> bool:
        # If both nodes are null, they are equivalent
        if not node1 and not node2:
            return True
        # If only one is null, they are not equivalent
        if not node1 or not node2:
            return False

        # Check if current nodes have the same value and 
        # (1) their children match directly or 
        # (2) their children match when flipped
        return (node1.val == node2.val and 
               ((self.dfs(node1.left, node2.left) and self.dfs(node1.right, node2.right)) or 
                (self.dfs(node1.left, node2.right) and self.dfs(node1.right, node2.left))))

    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.dfs(root1, root2)