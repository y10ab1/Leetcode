# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        map_inorder = {}
        for i, val in enumerate(inorder): map_inorder[val] = i
        def recur(low, high, Ps, Pe):
            if low > high: return None
            x = TreeNode(postorder[Pe])
            print(x.val)
            mid = map_inorder[x.val]
            x.right = recur(mid+1, high, Ps+mid-low, Pe-1)
            
            x.left = recur(low, mid-1, Ps, Ps+mid-low-1)
            return x
        return recur(0, len(inorder)-1, 0, len(postorder)-1)