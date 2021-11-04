class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l<r:
            m = (l+r)//2
            if m*m < x:
                l = m+1
            elif m*m > x:
                r = m
            else:
                return m
        if l*l > x:
            return l-1
        else:
            return l