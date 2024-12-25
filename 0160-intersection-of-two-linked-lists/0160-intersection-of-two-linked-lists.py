# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # The value of the node
        self.next = next  # Pointer to the next node

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # If either of the lists is empty, return None (no intersection)
        if not headA or not headB:
            return None

        # Initialize two pointers, pA and pB, starting at the heads of list A and list B respectively
        pA, pB = headA, headB

        # Traverse both lists until either the intersection node is found or both pointers reach the end (None)
        while pA != pB:
            # Move pA to the next node in list A, or switch to the head of list B if pA reaches the end
            pA = headB if pA is None else pA.next
            # Move pB to the next node in list B, or switch to the head of list A if pB reaches the end
            pB = headA if pB is None else pB.next

        # Return the node where the two pointers meet, which is the intersection node,
        # or None if no intersection exists (both will reach None simultaneously)
        return pA
