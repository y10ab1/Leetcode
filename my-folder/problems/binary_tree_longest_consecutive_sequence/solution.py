# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node, maxlen):
            leftmax, rightmax = maxlen, maxlen
            if node.left:
                if node.left.val == node.val+1:
                    leftmax = max(maxlen,dfs(node.left, maxlen+1))
                else:
                    leftmax = max(maxlen,dfs(node.left, 1))
            if node.right:
                if node.right.val == node.val+1:
                    rightmax = max(maxlen,dfs(node.right, maxlen+1))
                else:
                    rightmax = max(maxlen,dfs(node.right, 1))
            return max(leftmax, rightmax)
        return dfs(root,1)