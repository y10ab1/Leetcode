# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def dfs(node:int, dep:int, depth:int):
            if not node:
                return
            if dep+1 == depth:
                node.left = TreeNode(val=val,left=node.left)
                node.right = TreeNode(val=val,right=node.right)
            if depth > dep:
                dfs(node.left,dep+1,depth)
                dfs(node.right,dep+1,depth)
            
        if depth==1:
            root = TreeNode(val=val,left=root)
        else:
            dfs(root,1,depth)
        return root