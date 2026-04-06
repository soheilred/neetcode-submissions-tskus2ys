"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # newHead = Node(head.val)
        prev = Node(0)
        newhead = prev
        newNodes = {}
        cur = head

        while cur:
            if cur not in newNodes:
                newNode = Node(cur.val)
                newNodes[cur] = newNode

            # create the next node
            if cur.next and cur.next not in newNodes:
                newNext = Node(cur.next.val)
                newNodes[cur.next] = newNext

            newNodes[cur].next = newNodes[cur.next] if cur.next else None

            # create the random node
            if cur.random and cur.random not in newNodes:
                rand = Node(cur.random.val)
                newNodes[cur.random] = rand
                
            newNodes[cur].random = newNodes[cur.random] if cur.random else None

            prev.next = newNodes[cur]
            # if cur.random: 
            #     prev.random = newNodes[cur.random]

            prev = newNodes[cur]
            # newHead = newHead.next
            cur = cur.next


        # return newNodes[list(newNodes.keys())[1]]
        return newhead.next

        