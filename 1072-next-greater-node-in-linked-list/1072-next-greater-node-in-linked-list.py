# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return []

        # Convert linked list to a list
        values = []
        while head:
            values.append(head.val)
            head = head.next

        n = len(values)
        result = [0] * n
        stack = []

        for i in range(n):
            while stack and values[i] > values[stack[-1]]:
                j = stack.pop()
                result[j] = values[i]
            stack.append(i)

        return result