# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        indexmap = {}
        for i in range(len(inorder)) : indexmap[inorder[i]] = i
        def build(preorder, inorder, low, high):            
            if low>high or len(preorder) == 0: return
            root = TreeNode()
            root.val = preorder[0]
            
            del preorder[0]
            
            mid = indexmap[root.val]
            
            
            root.left = build(preorder, inorder, low, mid-1)
            root.right = build(preorder, inorder, mid+1, high)
            
            return root
        root = build(preorder, inorder, 0, len(inorder)-1)
        return root
        
        