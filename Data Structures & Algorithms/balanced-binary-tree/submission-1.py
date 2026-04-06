# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)

        # def height(root):
        #     if not root:
        #         return 0
            
        #     return 1 + max(height(root.left), height(root.right))

        # left = height(root.left)
        # right = height(root.right)
        # return abs(left - right) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
        res = dfs(root)
        return True if res != -1 else False
        