# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        bal = True

        def height(root):
            if not root:
                return 0
                
            nonlocal bal
            
            left = 1 + height(root.left)
            right = 1 + height(root.right)

            if abs(left - right) > 1:
                bal = False

            return max(left, right)

        height(root)

        return bal
        