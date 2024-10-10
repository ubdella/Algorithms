class Solution:
    def kthSmallest(self, root, k):
        self.k = k
        self.result = None
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            
            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return
            
            dfs(node.right)
        
        dfs(root)
        return self.result