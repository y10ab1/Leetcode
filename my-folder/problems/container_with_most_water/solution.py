class Solution:
    def maxArea(self, height: List[int]) -> int:
        L,R = 0, len(height)-1
        area = 0
        while L < R:
            h = min(height[L], height[R])
            area = max(area, h*(R-L))
            while height[L] == h and L<R:
                L+=1
            while height[R] == h and L<R:
                R-=1
        return area
        