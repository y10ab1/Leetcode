# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.preval = None
        self.ans = True
        def inorder(node):
            if not self.ans or not node:
                return
            inorder(node.left)
            
            if self.preval != None and self.preval >= node.val:
                self.ans = False
            self.preval = node.val
            
            inorder(node.right)
        
        inorder(root)
        return self.ans
                
            