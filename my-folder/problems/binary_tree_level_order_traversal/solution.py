# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.queue = []
        self.ans = []
        self.Deep = []
        def BFS(root, deep):
            queue = []
            if len(self.Deep) < deep+1:
                self.Deep.append([])
            
            if root.left:
                queue.append(root.left)
                self.Deep[deep].append(root.left.val)
            if root.right:
                queue.append(root.right)
                self.Deep[deep].append(root.right.val)
            while len(queue) != 0:
                BFS(queue.pop(0),deep+1)
            
        if not root : return []
        self.Deep.append([root.val])
        BFS(root , 1)
        for i in range(len(self.Deep)):
            if self.Deep[i]:
                self.ans.append(self.Deep[i])
        return self.ans