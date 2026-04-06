# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        prev = l2
        newNode = l2

        while l1 and l2:
            val = l1.val + l2.val + carry
            l2.val = val % 10
            carry = val // 10
            prev = l2
            l1 = l1.next
            l2 = l2.next
        
        rem = l1 or l2
        prev.next = rem

        while rem:
            tmp = rem.val + carry
            rem.val = tmp % 10
            carry = tmp // 10
            prev = rem
            rem = rem.next
        
        if carry:
            prev.next = ListNode(carry)
        
        return newNode
        