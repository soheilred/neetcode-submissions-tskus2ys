# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque([root])
        res = ""

        while q:
            cur = q.popleft()
            res += str(cur.val) + '|' if cur else '.|'
            if cur:
                q.append(cur.left)
                q.append(cur.right)
        
        l = len(res)
        while res[l-2:l] == '.|':
            l -= 2

        print(res[:l])
        return res[:l-1]

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split('|')
        print(nodes)
        if len(nodes) == 1:
            return TreeNode(nodes[0]) if nodes[0] != '.' else None
        root = TreeNode()
        parent = TreeNode()
        q = deque([(root, parent, 'r')])
        for n in nodes:
            node, par, child = q.popleft()
            if n == '.':
                # node = None
                # del node
                continue

            node.val = n
            if child == 'l': par.left = node
            elif child == 'r': par.right = node
            q.append((TreeNode(), node, 'l'))
            q.append((TreeNode(), node, 'r'))
        
        return root

