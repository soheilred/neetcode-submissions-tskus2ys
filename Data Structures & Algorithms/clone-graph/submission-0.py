"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        head = Node(node.val) # new graph
        stack = [node] # original graph
        nodes_dict = {head.val: head} # mapping val: node
        # seen = [False] * n
        seen = set()

        while stack:
            cur = stack.pop()
            if cur not in seen:
                seen.add(cur)
                for neighbor in cur.neighbors:
                    if neighbor.val not in nodes_dict:
                        new_node = Node(neighbor.val)
                        nodes_dict[neighbor.val] = new_node
                    nodes_dict[cur.val].neighbors.append(nodes_dict[neighbor.val])
                    stack.append(neighbor)
                # else:
        return head




        