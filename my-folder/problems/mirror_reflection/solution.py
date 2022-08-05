class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # coord. 2: even, odd      
        # coord. 1: odd, odd
        # coord. 0: odd, even
        m = (abs(q*p)//math.gcd(p,q))
        y = m//p
        x = m//q
        
        if x%2 == 0 and y%2 !=0:
            return 2
        elif x%2 != 0 and y%2 ==0:
            return 0
        else:
            return 1
        