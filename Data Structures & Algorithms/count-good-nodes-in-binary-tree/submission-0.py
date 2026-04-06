# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        count = 0
        
        def good(node, max_sf):
            if not node:
                return
            nonlocal count
            
            if node.val >= max_sf:
                count += 1
                max_sf = node.val
            
            good(node.left, max_sf)
            good(node.right, max_sf)
        
        good(root, root.val)
        return count
            
            
