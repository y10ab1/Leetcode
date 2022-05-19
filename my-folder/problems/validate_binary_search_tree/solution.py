# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.previous_val = float('-inf')
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root:
            if not self.isValidBST(root.left):
                return False
            
            if root.val <= self.previous_val:
                return False
            
            self.previous_val = root.val
            
            if not self.isValidBST(root.right):
                return False
        
        return True
    
    
        