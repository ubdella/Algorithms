# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        def dfs(root):
            send = [0, 0, None]            
            if not root:
                return send
            
            l, r = dfs(root.left), dfs(root.right)
            
            if l[0] or r[0] or root == p:
                send[0] = 1
            if l[1] or r[1] or root == q:
                send[1] =1
            if not send[2]:
                if l[2]:
                    send[2] = l[2]
                if r[2]:
                    send[2] = r[2]            
            if send[0] and send[1] and not send[2]:
                send[2]=root
                

            print(send)
            return send
        
        return dfs(root)[2]