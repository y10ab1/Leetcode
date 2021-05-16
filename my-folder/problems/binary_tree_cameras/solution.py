# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.cnt = 0
        def dfs(root):
            #0 == leaf
            #1 == leaf parent
            #2 == coverd
            if not root: return 2
            l, r = dfs(root.left), dfs(root.right)
            if l == 0 or r == 0:
                self.cnt += 1
                return 1
            return 2 if l == 1 or r == 1 else 0
        return (dfs(root)==0) +self.cnt