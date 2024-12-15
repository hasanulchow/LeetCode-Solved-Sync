# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Detect if a linked list has a cycle using the Floyd's Cycle Detection Algorithm.
        :param head: The head node of the linked list.
        :return: True if there is a cycle, False otherwise.
        """
        
        # Initialize two pointers: fast and slow, both starting at the head of the list.
        fast = head
        slow = head

        # Traverse the linked list with the two pointers:
        # - `fast` moves two steps at a time.
        # - `slow` moves one step at a time.
        while fast and fast.next:
            fast = fast.next.next  # Move fast pointer two steps ahead.
            slow = slow.next  # Move slow pointer one step ahead.

            # If fast and slow pointers meet, it means there is a cycle.
            if fast == slow:
                return True

        # If the loop exits, it means fast reached the end of the list (no cycle).
        return False
