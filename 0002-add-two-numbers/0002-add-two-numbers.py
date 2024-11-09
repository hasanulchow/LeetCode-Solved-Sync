import itertools as it
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def forward(curr = None):
            if curr:
                yield curr.val
                for i in forward(curr.next):
                    yield i
        def add():
            root = ListNode(-1,None)
            ans = root
            straightL1 = forward(l1)
            straightL2 = forward(l2)
            carry = 0
            last = None
            for num1, num2 in it.zip_longest(straightL1, straightL2, fillvalue=0):
                val = carry+num1+num2
                if val <= 9:
                    carry = 0
                    ans.val = val
                    ans.next = ListNode(0, None)
                    last = ans
                    ans = ans.next
                else:
                    carry = val // 10
                    val -= 10
                    ans.val = val
                    ans.next = ListNode(0, None)
                    last = ans
                    ans = ans.next
            last.next = None
            if carry:
                last.next = ListNode(carry, None)
            return root
        return add()