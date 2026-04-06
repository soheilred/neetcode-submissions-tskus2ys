# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0

        def preorder(node):
            if not node:
                return
            
            nonlocal count
            # count += 1
            
            left = preorder(node.left)

            count += 1
            if count == k:
                return node.val
            
            right = preorder(node.right)

            return left or right
        
        return preorder(root)
            

        