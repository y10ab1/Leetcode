class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        while True:
            if n == 1:
                return True
            if n <= 0:
                return False
            n=n/3
