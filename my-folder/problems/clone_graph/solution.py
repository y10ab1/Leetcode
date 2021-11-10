"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        v = {}
        def dfs(r):
            c = Node(r.val)
            if v.get(r):
                return v[r]
            else:
                v[r] = c
            for n in r.neighbors:
                c.neighbors.append(dfs(n))
            return c
        
        croot = dfs(node)
        return croot
        