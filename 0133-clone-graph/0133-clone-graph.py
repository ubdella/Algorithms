"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def copy(node):
            if node in oldToNew:
                return oldToNew[node]
            new = Node(node.val)
            oldToNew[node] = new
            for n in node.neighbors:
                new.neighbors.append(copy(n))
            return new
        oldToNew = {}
        return copy(node) if node else None