# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        res = ListNode()
        sent = ListNode(next=res)
        carry = 0

        while cur1 and cur2:
            val = 0
            if cur1:
                val = cur1.val + carry
            if cur2:
                val += cur2.val
            carry = val // 10
            val = val % 10
        
            cur = ListNode(val)
            res.next = cur
            res = cur
            cur1 = cur1.next
            cur2 = cur2.next

        cur = cur1 if cur1 is not None else cur2

        while cur:
            val = carry + cur.val
            carry = val // 10
            val = val % 10
            res.next = ListNode(val)
            res = res.next
            cur = cur.next

        if carry:
            res.next = ListNode(carry)

        return sent.next.next
