# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        
        
        
        leftD = self.getD(root.left)
        rightD = self.getD(root.right)
        
        if leftD == rightD:
            return pow(2,leftD) + self.countNodes(root.right)
        else:
            return pow(2,rightD) + self.countNodes(root.left)
        
        
    def getD(self,node):
        if not node:
            return 0
        return 1+self.getD(node.left)
