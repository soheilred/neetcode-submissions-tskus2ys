# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = prev = ListNode()

        while lists:
            K = len(lists)

            min_ind, min_val = 0, float('inf')
            for i in range(K):
                if lists[i].val < min_val:
                    min_ind = i
                    min_val = lists[i].val
            
            prev.next = lists[min_ind]
            prev = lists[min_ind]
            lists[min_ind] = lists[min_ind].next
            if not lists[min_ind]:
                lists.pop(min_ind)
        
        return head.next

        