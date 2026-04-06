# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tails = []
        heads = []

        def reverse(head, tail):
            prev = head
            # new_tail = head
            cur = head.next
            while cur and cur != tail:
                cur.next, prev, cur = prev, cur, cur.next
            
            head.next = None

            # tail is the new head
            # cur.next = prev
            return prev, head
        
        right = head

        while right:
            left = right

            # goes inside a loop
            count = 0
            while count < k and right:
                # slow, fast = slow.next, fast.next.next
                right = right.next
                count += 1
            
            if count != k:
                break
            # print(left.val, right.val)
            
            # reverse from left to right
            r_left, r_right = reverse(left, right)
            tails.append(r_right)
            heads.append(r_left)
        
        for i in range(len(tails) - 1):
            tails[i].next = heads[i+1]
        
        if count != k:
            tails[-1].next = left

        return heads[0]    



        # def reverse(head, tail):
        #     prev, cur, n = tail, head, head.next
        #     first = head

        #     while n:
        #         cur.next = prev
        #         prev, cur, n = cur, n, n.next
            
        #     cur.next = prev

        #     return cur, first
        
        # count = 0
        # prev, cur = head, head

        # while True:
        #     p = cur
        #     while count < k and cur:
        #         count += 1
        #         p = cur
        #         cur = cur.next 
            
        #     if count == k:
        #         count = 0
        #         p.next = None
        #         reved_head, tail = reverse(prev, cur)
        #         # print(reved_head.val)
        #         # if tail: print(tail.val)
        #         tails.append(tail)
        #         heads.append(reved_head)
        #         prev = cur
            
            
        #     else:
        #         break
        
        # new_head = heads[0]
        # # heads[0].next = tails[1]
        
        # for i in range(len(tails) - 1):
        #     tails[i].next = heads[i+1]
        

        # return new_head
    

       