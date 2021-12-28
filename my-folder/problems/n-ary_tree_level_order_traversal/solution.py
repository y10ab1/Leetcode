"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque([root])
        def BFS(q):
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                q += node.children
                
            ans.append(level)
            if q:
                BFS(q)
        BFS(q)
        return ans