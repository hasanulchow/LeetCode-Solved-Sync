# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Constructs a binary tree from its inorder and postorder traversal arrays.

        :param inorder: List[int] - Inorder traversal of the binary tree.
        :param postorder: List[int] - Postorder traversal of the binary tree.
        :return: TreeNode - The root node of the constructed binary tree.
        """
        
        # Base case: If either traversal list is empty, the tree cannot be constructed.
        if not inorder or not postorder:
            return None

        # The last element in postorder traversal is the root of the current subtree.
        root = TreeNode(postorder[-1])

        # Find the index of the root in the inorder traversal to split the tree into left and right subtrees.
        index = inorder.index(postorder[-1])

        # Recursively build the left subtree using the left portion of inorder and postorder arrays.
        root.left = self.buildTree(inorder[:index], postorder[:index])

        # Recursively build the right subtree using the right portion of inorder and postorder arrays.
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])

        # Return the constructed root node.
        return root
