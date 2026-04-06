# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def same_tree(root, sub):
            if not root and sub:
                return False

            if not sub and root:
                return False
            
            if not root and not sub:
                return True

            # if not root or not sub:
                # return False
            
            if root.val == sub.val: 
                return same_tree(root.left, sub.left) and same_tree(root.right, sub.right)
                
            # else:
                # return dfs(root.left, sub) or dfs(root.right, sub)
            else:
                return False
            
        def dfs(root, sub):
            if not root:
                return False

            if same_tree(root, sub) or dfs(root.left, sub) or dfs(root.right, sub):
                return True
            
            return False
            
        
        return dfs(root, subRoot)
        