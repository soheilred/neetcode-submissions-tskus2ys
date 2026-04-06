# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        level = 0
        q = deque([(root, level)])
        res = []
        cur_res = []

        while q:
            cur, l = q.popleft()

            if l == level:
                cur_res.append(cur.val)
            
            else:
                res.append(cur_res)
                level += 1
                cur_res = [cur.val]
            
            if cur.left: q.append((cur.left, level+1))
            if cur.right: q.append((cur.right, level+1))
        
        res.append(cur_res)
        return res

        