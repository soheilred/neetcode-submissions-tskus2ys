# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return

        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def reverse(head, tail):
            # print(head.val, tail.val)
            prev = head
            cur = head.next
            # n = cur.next

            while cur:
                # print(cur.val)
                tmp = cur.next
                cur.next = prev
                prev, cur = cur, tmp
            
            head.next = None
            # cur.next = prev

            return prev
        
        right = reverse(slow, fast)
        slow.next = None

        left = head
        while left and right:
            n_l, n_r = left.next, right.next
            left.next, right.next = right, n_l
            left, right = n_l, n_r

        
        # # reverse the list from slow to fast
        # prev = slow
        # cur = slow.next
        # # n = cur.next
        # prev.next = None

        # while cur:
        #     # print(cur.val)
        #     tmp = cur.next
        #     cur.next = prev
        #     prev, cur = cur, tmp
        
        # # cur.next = prev

        # rev_head = prev
        # cur = head

        # while cur and rev_head:
        #     # new_head.next = head
        #     tmp = cur.next
        #     tmp_rev = rev_head.next
        #     cur.next = rev_head
        #     rev_head.next = tmp
        #     cur, rev_head = tmp, tmp_rev

        