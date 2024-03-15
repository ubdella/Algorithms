# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        i = root
        
        while i!=None:
            if p.val< i.val and q.val<i.val:
                i = i.left
            elif p.val > i.val and q.val> i.val:
                i = i.right
            elif p.val == i.val or q.val == i.val:
                return i
            else:
                return i
