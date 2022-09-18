class Solution:
    def trap(self, h: List[int]) -> int:
        ans = 0
        l,r = 0,len(h)-1
        maxl,maxr = 0,0
        
        while l<r:
            if h[l]<=h[r]:
                if maxl<=h[l]:
                    maxl=h[l]
                else:
                    ans+=maxl-h[l]
                l+=1
            else:
                if maxr<=h[r]:
                    maxr=h[r]
                else:
                    ans+=maxr-h[r]
                r-=1
        return ans