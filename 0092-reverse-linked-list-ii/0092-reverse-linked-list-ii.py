# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Reverse a portion of a singly linked list between positions `left` and `right` (1-indexed).
        :param head: The head of the singly linked list.
        :param left: The starting position of the portion to reverse (inclusive).
        :param right: The ending position of the portion to reverse (inclusive).
        :return: The head of the modified linked list.
        """
        
        # Edge case: If the list is empty or the range to reverse is a single element, return the head as-is.
        if not head or left == right:
            return head

        # Step 1: Create a dummy node pointing to the head to handle cases where the head is reversed.
        dummy = ListNode(0, head)
        prev = dummy  # `prev` will eventually point to the node just before the `left` position.

        # Step 2: Move `prev` to the node just before the `left` position.
        for _ in range(left - 1):
            prev = prev.next

        # Step 3: Reverse the sublist between `left` and `right`.
        # `cur` points to the first node in the sublist to reverse.
        cur = prev.next
        for _ in range(right - left):
            temp = cur.next  # Store the next node to be reversed.
            cur.next = temp.next  # Skip the node `temp` in the current sublist.
            temp.next = prev.next  # Insert `temp` at the beginning of the reversed sublist.
            prev.next = temp  # Update `prev.next` to point to the new head of the reversed sublist.

        # Step 4: Return the new head of the list, which is `dummy.next`.
        return dummy.next
