# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node pointing to the head of the list.
        # This helps handle cases where the head node itself might be removed.
        dummy = ListNode(0, head)
        curr = dummy  # Pointer to traverse the list.

        # Loop through the list while there are at least two more nodes to check.
        while curr.next and curr.next.next:
            # If the current node and the next node have the same value, it's a duplicate.
            if curr.next.val == curr.next.next.val:
                # Keep a pointer to the duplicate value.
                running = curr.next
                num = running.val  # Store the duplicate value.

                # Skip all nodes with the duplicate value.
                while running and running.val == num:
                    running = running.next

                # Connect the current node to the first non-duplicate node.
                curr.next = running
            else:
                # Move to the next node if there is no duplicate.
                curr = curr.next

        # Return the head of the modified list, skipping the dummy node.
        return dummy.next
