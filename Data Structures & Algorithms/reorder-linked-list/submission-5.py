# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return 
        s, f = head, head.next

        while f and f.next:
            s, f = s.next, f.next.next
        
        prev = s
        cur = prev.next
        prev.next = None

        while cur: # 6
            print(prev.val, cur.val)
            tmp = cur.next # tmp = 8
            cur.next = prev # fix cur
            prev, cur = cur, tmp # prev: 6, cur: 8

        right = prev
        left = head

        while right:
            tmp_l, tmp_r = left.next, right.next
            left.next, right.next = right, tmp_l
            if not right.next:
                break
            left, right = tmp_l, tmp_r
        
        


        