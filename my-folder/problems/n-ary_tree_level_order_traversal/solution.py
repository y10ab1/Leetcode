"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q = deque([root])
        ans = []
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if not node: continue
                q+=node.children
                level.append(node.val)
            if level:
                ans.append(level)
        return ans