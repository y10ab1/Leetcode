class Solution:
    def myPow(self, x: float, n: int) -> float:
        def p(x,n):
            if n == 0:
                return 1
            elif n % 2 == 0:
                return p(x*x,n//2)
            else :
                return x*p(x,n-1)
        if n >= 0:
            return p(x,n)
        else:
            return 1/p(x,-n)