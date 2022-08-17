# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = defaultdict(list)
        def dfs(node):
            if not node:
                return 0
            level = max(dfs(node.left), dfs(node.right)) +1
            self.ans[level].append(node.val)
            node.left, node.right = None, None
            return level
        dfs(root)
        ans = []
        for i in sorted(self.ans.keys()):
            ans.append(self.ans[i])
        return ans