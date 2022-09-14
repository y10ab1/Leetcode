# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        bitmask = 0
        self.ans = 0
        
        
        def dfs(node, bitmask):
            bit = 1<<(node.val - 1)
            bitmask^=bit
            
            if node.left: dfs(node.left, bitmask)
            if node.right: dfs(node.right, bitmask)
            
            if node.left == node.right:
                if not bitmask ^ (bitmask & -bitmask):
                    self.ans +=1
                    
        dfs(root, bitmask)
        return self.ans
            
                
            
        dfs(root, bitmask)
        return self.ans
            
            
            