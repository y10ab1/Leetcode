class Solution:
    def tribonacci(self, n: int) -> int:
        a0,a1,a2=0,1,1
        if n == 0:
            return 0
        elif n<3:
            return 1
        
        for i in range(3,n+1):
            t = a0+a1+a2
            a0,a1,a2 = a1,a2,t
            
        return a2