# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        seen = set()

        def lca(root, p, q):
            if not root or p.val == root.val or q.val == root.val:
                return root

            print(root.val, p.val, q.val)
            
            # if one of p or q is on the right
            left = lca(root.left, p, q)
            right = lca(root.right, p, q)
        
            if left and right:
                return root
            
            if left or right:
                return left or right
            

        return lca(root, p, q)
            

            
            
