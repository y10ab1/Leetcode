# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node: TreeNode) -> bool:
            if not node:
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if not left:
                node.left = None
            if not right:
                node.right = None
                
            if node.val == 1 or left or right:
                return True
            return False
        
        if dfs(root):
            return root    
        return None