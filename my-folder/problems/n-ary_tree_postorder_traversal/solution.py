"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stacks = [root]
        ans = []
        while len(stacks) > 0:
            if stacks[-1].children == []:
                ans.append(stacks.pop().val)
            if len(stacks)>0 and stacks[-1].children != []:
                temp = stacks[-1].children[::-1]
                stacks[-1].children = []
                stacks += temp
        return ans