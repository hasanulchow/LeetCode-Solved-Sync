# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: 
        # Base case: If the list of linked lists is empty, return None
        if not lists or len(lists) == 0:
            return None
        
        # Use iterative merging to reduce the number of lists
        while len(lists) > 1:
            temp = []  # Temporary list to store merged lists
            for i in range(0, len(lists), 2):  # Pair up lists two at a time
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                temp.append(self.merge_lists(l1, l2))  # Merge the two lists
            lists = temp  # Update the list of lists with the merged results
        
        # The final merged list is the only remaining list
        return lists[0]
    
    def merge_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to serve as the head of the merged list
        node = ListNode()
        ans = node  # Pointer to the start of the merged list
        
        # Merge the two lists by comparing their values
        while l1 and l2:
            if l1.val > l2.val:
                node.next = l2
                l2 = l2.next
            else:
                node.next = l1
                l1 = l1.next
            node = node.next  # Move to the next position in the merged list
        
        # Attach the remaining elements from either list
        if l1:
            node.next = l1
        else:
            node.next = l2
        
        return ans.next  # Return the merged list starting from the first real node
