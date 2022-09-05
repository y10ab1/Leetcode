# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = [0]
        def dfs(node: TreeNode, maxval:int):
            if not node:
                return
            if maxval <= node.val:
                ans[0]+=1
                maxval = node.val
            dfs(node.left, maxval)
            dfs(node.right, maxval)
        dfs(root, root.val)
        return ans[0]