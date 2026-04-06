# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def bs_maker(preord, inord):
            if len(preord) == 0 or len(inord) == 0:
                return
            root = TreeNode(preord[0])
            root_ind = inord.index(root.val)
            left_inord = inord[:root_ind]
            right_inord = inord[root_ind:]
            i = 1
            while i < len(preord) and preord[i] in left_inord:
                i += 1

            left_preord = preord[1:i]
            right_preord = preord[i:]
            root.left = bs_maker(left_preord, left_inord)
            root.right = bs_maker(right_preord, right_inord)
            return root

        return bs_maker(preorder, inorder)

        