# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Create two dummy nodes to represent the smaller and larger partitions.
        slist, blist = ListNode(), ListNode()
        
        # Pointers to traverse and build the smaller and larger partitions.
        small, big = slist, blist

        # Traverse the original list.
        while head:
            # If the current node's value is smaller than x, add it to the smaller list.
            if head.val < x:
                small.next = head
                small = small.next
            else:
                # Otherwise, add it to the larger list.
                big.next = head
                big = big.next
                
            # Move to the next node in the original list.
            head = head.next

        # Connect the end of the smaller list to the beginning of the larger list.
        small.next = blist.next
        
        # End the larger list to avoid any cycles or dangling pointers.
        big.next = None

        # Return the head of the smaller list, which is now the head of the partitioned list.
        return slist.next
