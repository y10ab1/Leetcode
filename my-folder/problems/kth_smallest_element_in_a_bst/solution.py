# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        a = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            a.append(node.val)
            dfs(node.right)
        dfs(root)
        print(a)
        return a[k-1]