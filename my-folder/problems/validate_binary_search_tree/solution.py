# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(r):
            if not r:
                return 'None', 'None'
            leftmin, leftmax = dfs(r.left)
            rightmin, rightmax = dfs(r.right)
            if leftmax == 'False' or rightmin == 'False':
                return 'False', 'False'
            
            
            if leftmax == 'None' or rightmin == 'None':
                if rightmin == 'None' and leftmax == 'None':
                    return r.val, r.val
                elif leftmax == 'None' and r.val < rightmin:
                    return r.val, rightmax
                elif rightmin == 'None' and r.val > leftmax:
                    return leftmin, r.val
                else:
                    return 'False', 'False'
            else:
                if leftmax < r.val and r.val < rightmin:
                    return leftmin, rightmax
                else:
                    return 'False', 'False'
        
        ansl, ansr = dfs(root)
        if ansl == 'False' or ansr == 'False':
            return False
        else:
            return True