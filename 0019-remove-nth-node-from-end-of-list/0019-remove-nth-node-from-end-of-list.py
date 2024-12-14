# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Define the class `Solution` which contains the method to remove the nth node from the end of the list.
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Method to remove the nth node from the end of a linked list.

        res = ListNode(0, head)
        # Create a dummy node `res` to simplify edge cases (e.g., removing the head node).
        # `res.next` points to the actual head of the list.
        dummy = res
        # Initialize `dummy` to `res`. `dummy` will be used to traverse the list.

        for _ in range(n):
            # Move the `head` pointer `n` steps forward. This creates a gap of `n` nodes between `head` and `dummy`.
            head = head.next

        while head:
            # Move both `head` and `dummy` one step forward until `head` reaches the end of the list.
            # This ensures `dummy` points to the node before the one to be removed.
            head = head.next
            dummy = dummy.next

        dummy.next = dummy.next.next
        # Skip the nth node from the end by updating the `next` pointer of `dummy`.

        return res.next
        # Return the updated list, starting from the node after `res` (i.e., the original head if it wasn't removed).
