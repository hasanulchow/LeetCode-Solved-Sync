# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        """
        Initialize the iterator with the root node of the BST.
        The iterator will traverse the BST in an in-order manner.
        """
        # Initialize the generator for in-order traversal and get the first value.
        self.iter = self._inorder(root)
        self.nxt = next(self.iter, None)  # Store the next element if available.

    def _inorder(self, node: Optional[TreeNode]) -> Generator[int, None, None]:
        """
        Generator function to perform in-order traversal of the BST.
        :param node: TreeNode - The current node in the BST.
        :yield: int - The value of the node in in-order sequence.
        """
        if node:
            yield from self._inorder(node.left)  # Traverse the left subtree.
            yield node.val  # Yield the value of the current node.
            yield from self._inorder(node.right)  # Traverse the right subtree.

    def next(self) -> int:
        """
        Return the next smallest number in the BST.
        :return: int - The next in-order value.
        """
        res, self.nxt = self.nxt, next(self.iter, None)  # Get the current value and update `self.nxt`.
        return res

    def hasNext(self) -> bool:
        """
        Check if there is a next smallest number in the BST.
        :return: bool - True if there is another value, False otherwise.
        """
        return self.nxt is not None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
