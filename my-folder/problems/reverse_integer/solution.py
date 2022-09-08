class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        sign = 1
        if s[0] == "-":
            sign = -1
            s = s[1:]
        s = s[::-1]
        
        
        num = sign*int(s)
        if num > 2**31-1 or num < -2**31:
            return 0
        return num