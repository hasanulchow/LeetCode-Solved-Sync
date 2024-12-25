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
    # Function to reverse a linked list starting from the given head node
    def reverse(self, head: ListNode) -> ListNode:
        prev = None  # Initialize previous node as None (will be the new tail)
        curr = head  # Current node starts at the head of the list

        # Iterate through the linked list and reverse the pointers
        while curr:
            next_temp = curr.next  # Save the next node
            curr.next = prev  # Reverse the current node's next pointer
            prev = curr  # Move the prev pointer to the current node
            curr = next_temp  # Move to the next node in the original list

        return prev  # Return the new head (which is the previous node)

    # Function to check if the linked list is a palindrome
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head  # Slow pointer for the middle of the list
        fast = head  # Fast pointer to find the end of the list

        # Move slow pointer to the middle, fast pointer to the end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the list (starting from the slow pointer)
        rev = self.reverse(slow)
        
        # Compare the first half and the reversed second half node by node
        while rev:
            if head.val != rev.val:  # If values don't match, it's not a palindrome
                return False
            head = head.next  # Move to the next node in the first half
            rev = rev.next  # Move to the next node in the reversed second half

        return True  # If no mismatches, the list is a palindrome
