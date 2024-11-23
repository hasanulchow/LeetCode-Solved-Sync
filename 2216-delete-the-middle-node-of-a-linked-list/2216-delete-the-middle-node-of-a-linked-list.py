# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Case 1: If the list has only one node, we return None, since the middle node is the only node
        if not head.next:
            return None

        # Initialize two pointers: slow (will eventually point to the node before the middle) 
        # and fast (used to move twice as fast as slow)
        fast = slow = head
        
        # Traverse the list with the fast pointer moving two steps at a time and the slow pointer moving one step at a time
        # We stop when the fast pointer reaches the end of the list (or when fast.next.next is None).
        # By the time this loop finishes, slow will be pointing to the node just before the middle node.
        while fast and fast.next and fast.next.next and fast.next.next.next:
            fast = fast.next.next  # Move fast two steps forward
            slow = slow.next       # Move slow one step forward

        # Delete the middle node by changing the "next" pointer of the node before it (slow) to skip over the middle node.
        slow.next = slow.next.next
        
        # Return the modified list, starting from the head
        return head
