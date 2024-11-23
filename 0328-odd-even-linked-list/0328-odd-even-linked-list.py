class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Edge case when the list is empty (head is None)
        if head is None:
            return head

        # Step 2: Initialize pointers for odd and even nodes
        odd = head  # 'odd' will point to the first node (which is odd-indexed)
        even = odd.next  # 'even' will point to the second node (which is even-indexed)
        evenHead = even  # Keep a reference to the first even node to attach at the end of the odd nodes later

        # Step 3: Traverse the list and rearrange the nodes
        while even and even.next:
            # Step 3.1: Link the current odd node to the next odd node
            odd.next = even.next
            odd = odd.next  # Move the odd pointer to the next odd node
            
            # Step 3.2: Link the current even node to the next even node
            even.next = odd.next
            even = even.next  # Move the even pointer to the next even node

        # Step 4: Attach the first even node (evenHead) at the end of the odd nodes
        odd.next = evenHead

        # Step 5: Return the head of the modified list
        return head
