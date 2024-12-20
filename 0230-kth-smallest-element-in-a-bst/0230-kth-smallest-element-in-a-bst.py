class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        Find the k-th smallest element in a Binary Search Tree (BST).
        :param root: TreeNode - The root of the BST.
        :param k: int - The k-th position (1-indexed) of the smallest element to find.
        :return: int - The value of the k-th smallest element.
        """
        def inorder(node):
            """
            Generator function to perform an in-order traversal of the tree.
            :param node: TreeNode - The current node being processed.
            :yield: int - The value of the node in sorted order.
            """
            if not node:
                return
            # Traverse the left subtree (smaller elements in BST)
            yield from inorder(node.left)
            # Yield the value of the current node
            yield node.val
            # Traverse the right subtree (larger elements in BST)
            yield from inorder(node.right)

        # Initialize the generator to perform in-order traversal
        gen = inorder(root)

        # Iterate through the generator to get the k-th smallest element
        for _ in range(k):
            result = next(gen)
        
        # Return the k-th smallest value
        return result
