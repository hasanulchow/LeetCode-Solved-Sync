class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base case: if the list is empty or has one element, it is already sorted
        if not head or not head.next:
            return head
        
        # Step 1: Find the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Slow pointer is now at the middle
        mid = slow.next
        slow.next = None  # Break the list into two halves
        
        # Step 2: Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # Step 3: Merge the sorted halves
        return self.merge(left, right)
    
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Dummy node to make merging easier
        dummy = ListNode(0)
        tail = dummy
        
        # Step 4: Merge two sorted lists
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        # Step 5: Attach the remaining part of the list (if any)
        tail.next = l1 if l1 else l2
        
        # Return the merged list, skipping the dummy node
        return dummy.next
