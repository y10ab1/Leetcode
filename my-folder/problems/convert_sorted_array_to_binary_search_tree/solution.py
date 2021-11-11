# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(l,r):
            if l > r:
                return None
            m = (l+r)//2
            node = TreeNode(nums[m])
            node.right = build(m+1,r)
            node.left = build(l,m-1)
            return node
        root = build(0,len(nums)-1)
        return root