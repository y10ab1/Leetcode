class Solution:
    def isHappy(self, n: int) -> bool:
        def getn(num):
            totalsum = 0
            while num > 0:
                num, r = divmod(num,10)
                totalsum += r**2
            return totalsum
        
        s = n
        f = getn(n)
        ans = True
        while s != f and s!=1 and f!=1:
            s = getn(s)
            f = getn(getn(f))
            if s == f:
                ans = False
                break
            elif s == 1 or f == 1:
                break
        return ans
            