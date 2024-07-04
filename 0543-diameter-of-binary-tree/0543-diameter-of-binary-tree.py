# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # we need the max depth of the left and right subtrees. the result is their sum
        self.res = 0
        def maxDepth(root):

            if not root: return 0
            left, right = maxDepth(root.left), maxDepth(root.right)
            global res
            self.res = max(self.res, left+right)
            return max(left, right) + 1
        maxDepth(root)
        return self.res