# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = list1, list2
        head = ListNode()
        sentinel = ListNode(next=head)

        while cur1 or cur2:
            if cur1 and cur2:
                if cur1.val > cur2.val:
                    head.next = cur2
                    cur2 = cur2.next
                else:
                    head.next = cur1
                    cur1 = cur1.next

            elif cur1:
                head.next = cur1
                cur1 = cur1.next
            
            else:
                head.next = cur2
                cur2 = cur2.next
            
            head = head.next
            
        
        return sentinel.next.next
        