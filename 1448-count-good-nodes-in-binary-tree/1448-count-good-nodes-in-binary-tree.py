# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        n = 0
        def dfs(root, maxInPath):
            nonlocal n
            if not root: return
            if root.val >= maxInPath:
                n += 1
                maxInPath = root.val
            dfs(root.left, maxInPath)
            dfs(root.right, maxInPath)

        dfs(root, root.val)
        return n

