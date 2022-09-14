# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        nodes = set()
        self.ans = 0
        
        def dfs(node, s):
            if not node:
                return
            
            if node.val in s:
                s.remove(node.val)
            else:
                s.add(node.val)
                
            dfs(node.left, s.copy())
            dfs(node.right, s.copy())
            if not node.left and not node.right and len(s)<=1:
                self.ans+=1
                
            
        dfs(root, nodes.copy())
        return self.ans
            
            
            