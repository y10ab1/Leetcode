# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def find(node,p,q):
            if not node:
                return 0
            
            left = find(node.left,p,q)
            right = find(node.right,p,q)
            cur = 0
            if node.val == p.val or node.val==q.val:
                cur = 1
            cnt = left+right+cur
            
            if cnt == 2:
                
                self.ans = node
                cnt =1
            return cnt
            
        
        find(root,p,q)
        return self.ans