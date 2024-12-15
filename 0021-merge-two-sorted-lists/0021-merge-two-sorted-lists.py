# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into a single sorted linked list.
        :param list1: The head of the first sorted linked list.
        :param list2: The head of the second sorted linked list.
        :return: The head of the merged sorted linked list.
        """
        
        # Create a dummy node to serve as the starting point of the merged list.
        # This avoids handling special cases for the head node.
        dummy = ListNode()
        cur = dummy  # `cur` is used to build the new list.

        # Traverse both lists while there are nodes remaining in both.
        while list1 and list2:
            # Compare the values of the current nodes in both lists.
            # Append the smaller value to the merged list and move the pointer of that list forward.
            if list1.val > list2.val:
                cur.next = list2  # Attach the current node of list2 to the merged list.
                list2 = list2.next  # Move the pointer in list2 forward.
            else:
                cur.next = list1  # Attach the current node of list1 to the merged list.
                list1 = list1.next  # Move the pointer in list1 forward.

            # Move the `cur` pointer to the next node in the merged list.
            cur = cur.next

        # If one of the lists still has nodes left, append them directly
        # since they are already sorted.
        if list1:
            cur.next = list1  # Append the remaining nodes of list1.
        else:
            cur.next = list2  # Append the remaining nodes of list2.

        # The `dummy` node's `next` points to the head of the merged list.
        return dummy.next
