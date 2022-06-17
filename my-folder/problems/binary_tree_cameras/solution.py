# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        val, ans = self.dfs(root)
        return (val == 0) + ans
        
    def dfs(self, node: Optional[TreeNode]):
        # 0 for leaf
        # 1 for leaf's parent
        # 2 for covered node
        
        if node == None:
            return (2, 0)
        
        (l,camleft), (r, camright) = self.dfs(node.left), self.dfs(node.right)
        ans = (camleft+camright)
        
        if l == 0 or r == 0:
            ans += 1
            return (1, ans)
        
        return (2, ans) if l == 1 or r == 1 else (0, ans)