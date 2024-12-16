# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # If the list is empty or has only one node, or k is zero, return the head as is.
        if not head or not head.next or k == 0:
            return head

        # Create a dummy node that points to the head.
        # This helps handle rotations cleanly.
        zero = ListNode(next=head)

        # Count the number of nodes in the list.
        count, tail = 0, zero
        while tail.next:
            count += 1
            tail = tail.next

        # Update k to be within the range of the list's length.
        # Rotating a list `count` times results in the same list.
        k = k % count
        if k == 0:  # No rotation needed if k is 0 after the modulo operation.
            return head

        # Find the new tail of the rotated list (count - k steps from the start).
        newTail = zero
        for _ in range(count - k):
            newTail = newTail.next

        # Update pointers to perform the rotation.
        zero.next = newTail.next  # New head becomes the node after the new tail.
        tail.next = head          # Old tail points to the old head, making it circular.
        newTail.next = None       # Break the circular connection to finalize the rotation.

        # Return the new head of the rotated list.
        return zero.next
