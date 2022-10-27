class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        A = [(i,j) for i,row in enumerate(img1) for j,_ in enumerate(row) if img1[i][j]]
        B = [(i,j) for i,row in enumerate(img2) for j,_ in enumerate(row) if img2[i][j]]
        cnt = collections.Counter((ax-bx,ay-by) for ax,ay in A for bx,by in B)
        return max(cnt.values() or [0])