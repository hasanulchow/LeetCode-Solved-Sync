class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy head node to simplify handling the result linked list
        dummyHead = ListNode(0)
        # Tail is used to build the result list step by step
        tail = dummyHead
        # Carry stores the carry-over value when summing digits
        carry = 0

        # Loop while there are nodes left in either list or there's a carry-over
        while l1 is not None or l2 is not None or carry != 0:
            # Get the value from l1 and l2, defaulting to 0 if the node is None
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            # Calculate the sum of the two digits and carry
            sum = digit1 + digit2 + carry
            # The new digit is the sum modulo 10
            digit = sum % 10
            # The new carry is the sum divided by 10 (integer division)
            carry = sum // 10

            # Create a new node with the resulting digit
            newNode = ListNode(digit)
            # Attach the new node to the tail of the result list
            tail.next = newNode
            # Move the tail pointer to the new node
            tail = tail.next

            # Move to the next nodes in l1 and l2 if they exist
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        # Return the result list, starting after the dummy head node
        result = dummyHead.next
        # Set the dummy head next to None to break the reference
        dummyHead.next = None
        return result
