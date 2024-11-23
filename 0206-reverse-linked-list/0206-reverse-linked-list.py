# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Initialize pointers
        prev = None           # Initially, there's no previous node for the head.
        current = head        # The current node starts as the head of the list.
        
        # Step 2: Traverse through the list and reverse the links.
        while current:
            # Step 2.1: Save the next node (to avoid losing track of the rest of the list)
            next_node = current.next  # 'next_node' temporarily stores the next node.
            
            # Step 2.2: Reverse the link of the current node
            current.next = prev      # The 'next' of the current node now points to the previous node.
            
            # Step 2.3: Move the prev and current pointers one step forward.
            prev = current           # 'prev' moves to the current node (becomes the previous node for the next iteration).
            current = next_node      # 'current' moves to the next node in the list.
        
        # Step 3: Return the new head of the reversed list.
        return prev  # After the loop, 'prev' will be the new head of the reversed list.

        