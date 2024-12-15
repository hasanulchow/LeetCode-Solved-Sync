"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Creates a deep copy of a linked list where each node contains a random pointer
        that could point to any node in the list or be None.
        :param head: The head of the input linked list.
        :return: The head of the copied linked list.
        """
        if not head:
            return None  # If the input list is empty, return None.
        
        # Step 1: Create new nodes and interweave them with the original list.
        # For each node in the original list, create a new node with the same value,
        # and insert it right after the original node.
        curr = head
        while curr:
            # Create a new node with the same value as the current node.
            new_node = Node(curr.val, curr.next)
            curr.next = new_node  # Link the new node after the current node.
            curr = new_node.next  # Move to the next original node.
        
        # Step 2: Copy the random pointers for the new nodes.
        # For each original node, assign the new node's random pointer to the next node of the original's random pointer.
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next  # Set the random pointer of the new node.
            curr = curr.next.next  # Move to the next original node.
        
        # Step 3: Separate the interwoven lists into the original and the copied list.
        old_head = head  # Pointer to traverse the original list.
        new_head = head.next  # Pointer to traverse the new list and will be the head of the copied list.
        curr_old = old_head  # Temporary pointer for the original list.
        curr_new = new_head  # Temporary pointer for the copied list.
        
        while curr_old:
            curr_old.next = curr_old.next.next  # Restore the next pointer for the original node.
            curr_new.next = curr_new.next.next if curr_new.next else None  # Restore the next pointer for the copied node.
            curr_old = curr_old.next  # Move to the next original node.
            curr_new = curr_new.next  # Move to the next copied node.
        
        # Return the head of the copied list.
        return new_head

        