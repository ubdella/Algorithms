class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}

        def dfs(cur):
            if cur in oldToNew:
                return oldToNew[cur]
            
            clone = Node(cur.val)
            oldToNew[cur] = clone
            
            for nei in cur.neighbors:
                clone.neighbors.append(dfs(nei))
            
            return clone
        
        return dfs(node)