"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        Connects each node in a binary tree to its next right node. If there is no next right node, 
        the 'next' pointer should be set to None. The tree is modified in place.

        :param root: Node - The root of the binary tree.
        :return: Node - The root of the binary tree with updated 'next' pointers.
        """
        
        # If the tree is empty, return None.
        if root is None:
            return None

        # Initialize the head pointer to the root node of the tree.
        head = root

        # Traverse levels of the tree.
        while head:
            # Temporary node to build the next level's connections.
            temp = Node()
            cur = temp  # Pointer to iterate and connect nodes at the current level.

            # Traverse the current level.
            while head:
                # If the current node has a left child, connect it.
                if head.left:
                    cur.next = head.left
                    cur = cur.next

                # If the current node has a right child, connect it.
                if head.right:
                    cur.next = head.right
                    cur = cur.next

                # Move to the next node at the same level.
                head = head.next

            # Move to the next level by pointing head to the first node in the next level.
            head = temp.next

        # Return the root node after all 'next' pointers are set.
        return root
