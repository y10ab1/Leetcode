class Solution:
    def fib(self, n: int) -> int:
        a0 = 0
        a1 = 1
        
        if n == 0 or n == 1:
            return n
        
        for i in range(2, n+1):
            a0, a1 = a1, a0 + a1
            
        return a1
            