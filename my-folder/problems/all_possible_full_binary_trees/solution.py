# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        sb = defaultdict(list)
        sb[1].append(TreeNode())
        for i in range(3,n+1)[::2]:
            
            for j in range(1,i)[::2]:
                for k in sb[j]:
                    for l in sb[i-1-j]:
                        node = TreeNode()
                        node.left = k
                        node.right = l
                        sb[i].append(node)
        return sb[n]
                
        