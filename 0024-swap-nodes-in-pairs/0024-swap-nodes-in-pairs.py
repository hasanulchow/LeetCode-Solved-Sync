# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # The value of the node
        self.next = next  # Pointer to the next node

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node which simplifies edge cases (e.g., an empty list or a list with a single node)
        dummy = ListNode(0, head)
        prev, cur = dummy, head  # Initialize pointers: 'prev' is the dummy node, 'cur' is the head of the list

        # Traverse the list in pairs
        while cur and cur.next:
            # 'npn' holds the pointer to the next pair after the current pair
            npn = cur.next.next
            # 'second' is the second node in the current pair
            second = cur.next

            # Swap the current pair:
            second.next = cur  # Make the second node point to the first node
            cur.next = npn  # Make the first node point to the next pair's first node
            prev.next = second  # The previous node now points to the second node in the pair

            # Move the pointers for the next iteration:
            prev = cur  # 'prev' now becomes the first node in the swapped pair
            cur = npn  # 'cur' moves to the first node of the next pair
        
        return dummy.next  # Return the new head of the modified list (next of dummy)
