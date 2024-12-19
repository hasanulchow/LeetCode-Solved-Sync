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
        self.stack = []  # Stack to simulate in-order traversal
        self._pushLeft(root)  # Push all left nodes of the tree into the stack

    def _pushLeft(self, node: Optional[TreeNode]):
        """
        Helper function to push all the left nodes of a tree/subtree to the stack.
        """
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        Return the next smallest number in the BST.
        :return: int - The next in-order value.
        """
        # Pop the top node from the stack (this is the next smallest element)
        node = self.stack.pop()
        # After popping, if the node has a right child, push its leftmost nodes to the stack
        self._pushLeft(node.right)
        return node.val

    def hasNext(self) -> bool:
        """
        Check if there is a next smallest number in the BST.
        :return: bool - True if there is another value, False otherwise.
        """
        # If the stack is not empty, we have another node to visit
        return len(self.stack) > 0
