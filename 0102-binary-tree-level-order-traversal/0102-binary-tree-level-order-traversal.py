# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        if not root:
            return []
        q.append(root)
        while q:
            level = []
            qLen = len(q)
            while qLen:
                n = q.popleft()
                qLen-=1
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                level.append(n.val)
            res.append(level)
        return res
                