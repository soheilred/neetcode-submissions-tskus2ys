# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        level = 0
        q = deque([(root, level)])
        res = [root.val]

        while q:
            cur, l = q.popleft()

            if l != level:
                level += 1
                res.append(cur.val)
            
            if cur.right: q.append((cur.right, level + 1))
            if cur.left: q.append((cur.left, level + 1))
        
        return res

        