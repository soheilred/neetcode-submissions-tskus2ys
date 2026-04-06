# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -float('inf')

        def bt(root):
            if not root:
                return 0
            nonlocal max_sum
            
            left = bt(root.left)
            right = bt(root.right)
            cur_max = max(left + right + root.val, left + root.val, right + root.val, root.val)

            if cur_max > max_sum:
                max_sum = cur_max
            
            return max(right + root.val, left + root.val, root.val)
        
        bt(root)
        return max_sum
        