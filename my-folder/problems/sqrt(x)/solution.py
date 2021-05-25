class Solution:
    def mySqrt(self, x: int) -> int:
        def BS(t,low,high):
            mid = (low + high)//2
            print(mid)
            if mid**2 <=t and (mid+1)**2 > t: return mid
            elif mid**2 > t: return BS(t,low,mid-1)
            elif mid**2 < t: return BS(t,mid+1,high)
        print("---")
        return BS(x,0,x)
        