# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        
        def dfs(node:Optional[TreeNode], sumval: int)->List[List[int]]:
            # if node is a leaf
            if not node.left and not node.right and node.val+sumval == targetSum:
                return [[node.val]]
            
            ret = []
            if node.left:
                ret += dfs(node.left, node.val+sumval)
            if node.right:
                ret += dfs(node.right, node.val+sumval)
            
            for l in ret:
                l.append(node.val)
            
            return ret
        
        ret = dfs(root, 0) if root else []

        return [l[::-1] for l in ret]
                