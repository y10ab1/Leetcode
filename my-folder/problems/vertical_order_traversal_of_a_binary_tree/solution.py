# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        ans = []
        
        def dfs(node,i,j):
            if not node:
                return
            d[j].append((i,node.val))
            dfs(node.left,i+1,j-1)
            dfs(node.right,i+1,j+1)   
            return
        dfs(root,0,0)
        for k in sorted(d.keys()):
            d[k].sort()
            temp = [i for _,i in d[k]]
            ans.append(temp)
        return ans