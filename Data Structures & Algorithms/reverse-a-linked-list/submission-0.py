# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        if not head:
            return head

        n = cur.next
        cur.next = None
        
        while n:
            tmp = n.next
            n.next = cur
            cur = n
            n = tmp
        
        return cur
        