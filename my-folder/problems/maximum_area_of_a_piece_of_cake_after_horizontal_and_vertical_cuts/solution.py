class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        maxw, maxh = 0,0
        pre = 0
        horizontalCuts.sort()
        verticalCuts.sort()
        
        for i in horizontalCuts:
            maxh = max(maxh, i-pre)
            pre = i
        maxh = max(maxh, h-pre)
        
        pre = 0
        for i in verticalCuts:
            maxw = max(maxw, i-pre)
            pre = i
        maxw = max(maxw, w-pre)
        
        
        return int((maxw*maxh) % (10**9+7))