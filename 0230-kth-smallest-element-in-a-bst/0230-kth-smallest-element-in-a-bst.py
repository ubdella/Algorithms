class Solution:
    def kthSmallest(self, root, k):
        result = None
        
        def dfs(node):
            nonlocal k
            nonlocal result
            if not node:
                return
            
            dfs(node.left)
            
            k -= 1
            if k == 0:
                result = node.val
                return
            
            dfs(node.right)
        
        dfs(root)
        return result