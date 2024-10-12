class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {node : Node(node.val)}

        stack = [node]
        
        while stack:
            cur = stack.pop()
            for nei in cur.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    stack.append(nei)
                oldToNew[cur].neighbors.append(oldToNew[nei])
        
        return oldToNew[node]
                    