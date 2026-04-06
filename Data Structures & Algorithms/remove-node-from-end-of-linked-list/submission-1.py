# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return head
        if not head.next:
            if n == 1: return head.next
            else: return head

        s, f = head, head.next.next
        l = 1

        while f and f.next:
            s = s.next
            f = f.next.next
            l += 1
        
        if f:
            l = 2 * l + 1
        else:
            l = 2 * l
        
        print(l)

        proc = l - n
        if proc == 0: return head.next
        cur = head

        while proc > 1:
            cur = cur.next
            proc -= 1
        
        if cur.next: 
            cur.next = cur.next.next
        return head

        