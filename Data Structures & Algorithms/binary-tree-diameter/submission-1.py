# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        d = 0

        def height(root):
            if not root:
                return 0
            nonlocal d
            
            l = height(root.left)
            r = height(root.right)
            d = max(d, l + r)
            return 1 + max(l, r)
        height(root)
        return d
        
        # def treelen(root):
        #     if not root:
        #         return 0
            
        #     return 1 + max(treelen(root.left), treelen(root.right))


        # left = treelen(root.left)
        # right = treelen(root.right)
        # return max(abs(left + right), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        