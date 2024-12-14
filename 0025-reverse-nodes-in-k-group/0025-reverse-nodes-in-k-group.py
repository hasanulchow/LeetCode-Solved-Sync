# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Define the class `Solution` which contains the method to reverse nodes in groups of k.

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Method to reverse every k nodes in a linked list. If the number of remaining nodes is less than k, they are left as-is.

        if not head or k == 1:
            # If the list is empty or k is 1 (no reversal needed), return the original head.
            return head

        dummy = ListNode(0)
        # Create a dummy node to act as a placeholder before the head of the list.
        dummy.next = head
        # Point the dummy node to the head of the linked list.
        prev = dummy
        # `prev` will track the node before the group being reversed.
        curr = head
        # `curr` starts at the head and is used to count and traverse the nodes.

        # Count the number of nodes in the linked list
        count = 0
        while curr:
            # Traverse the list to find the total number of nodes.
            count += 1
            curr = curr.next
            # Move to the next node.

        # Reverse k nodes at a time
        while count >= k:
            # Repeat the reversal process as long as there are at least k nodes left.
            curr = prev.next
            # `curr` points to the first node in the group to be reversed.
            nxt = curr.next
            # `nxt` points to the next node after `curr`.

            # Reverse the k nodes in the current group
            for _ in range(1, k):
                # Perform k-1 swaps to reverse the group.
                curr.next = nxt.next
                # Detach `nxt` from its current position and point `curr` to the node after `nxt`.
                nxt.next = prev.next
                # Insert `nxt` at the beginning of the group.
                prev.next = nxt
                # Update the start of the reversed group to `nxt`.
                nxt = curr.next
                # Move `nxt` to the next node to be processed.

            prev = curr
            # Move `prev` to the end of the reversed group, which is now `curr`.
            count -= k
            # Reduce the count by k since we've processed one group.

        return dummy.next
        # Return the new head of the list, which is the next node of the dummy.

